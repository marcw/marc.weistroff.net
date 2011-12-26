public: yes
tags: [code, php]
summary: |
    The one where I talk about SPL exceptions in PHP 5.

Semantic Coding?
================

Don’t worry. Semantic coding is not a new concept. Actually, you’re already
doing it each time you code. At least, I hope for you and your teammates.  The
principle of semantic coding is simple and is a great part of what we all name
“code readability”.

Look at those 2 pieces of code:

.. sourcecode:: php

    class A
    {
        public function A($a, $b)
        {
            return $a + $b;
        }

        public function B($a, $b)
        {
            return $a - $b;
        }

        public function C($a, $b)
        {
            return $a / $b;
        }

        public function D($a, $b)
        {
            return $a * $b;
        }
    }

This is not semantic code.

.. sourcecode:: php

    class Calculator
    {
        public function Add($a, $b)
        {
            return $a + $b;
        }

        public function Substract($a, $b)
        {
            return $a - $b;
        }

        public function Divide($a, $b)
        {
            return $a / $b;
        }

        public function Multiply($a, $b)
        {
            return $a * $b;
        }
    }

This is semantic code.

The difference between the two is that the second example class and method
names carry a meaning. When reading the code, you don’t have to remember what
the ‘Add’ method does because it’s clearly indicated within its name.

In the first example, you have to remember which method name does what. In the
second example, what the method does is its name. It’s a major difference.

Speaking in cognitive terms. Writing code should be a high cognitive effort in
order for the reading process to be a low cognitive effort.

Don’t forget that code is often read 100x time more that it’s written!

Now let’s apply semantic coding principle to exceptions!

Too much sfException is bad for the health
------------------------------------------

The use of sfException is a commong thing among all symfony projects’ code I
have the chance to read. While it’s harmless to use it from time to time, I
think that using nearly only sfException in your code is like using $a, $b or
$c as unique variable name.

What is sfException?
....................

As the sfException phpDoc says: > sfException is the base class for all symfony
related exceptions and provides an additional method for printing up a detailed
view of an exception.

If you look at the code of
`sfException <http://trac.symfony-project.org/browser/branches/1.4/lib/exception/sfException.class.php>`_
you’ll see that sfException has a bunch of tool to wrap an exception inside an
sfException. That’s why when an exception of any kind is thrown in symfony, you
see a nice html output.

In a symfony application, every thrown exception that bubbles up is eventually
catched in the
`sfFrontWebController <http://trac.symfony-project.org/browser/branches/1.4/lib/controller/sfFrontWebController.class.php#L23>`_
class. Then this exception is wrapped into an sfException one and is displayed
to the user.

The catching mechanism
~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: php

    // sfFrontWebController.class.php
    try
    {
      // application running...
      [...]
    }
    catch (sfException $e)
    {
      $e->printStackTrace();
    }
    catch (Exception $e)
    {
      sfException::createFromException($e)->printStackTrace();
    }

The wrapping mechanism
~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: php

    // sfException.class.php
    static public function createFromException(Exception $e)
    {
      $exception = new sfException(sprintf('Wrapped %s: %s', get_class($e), $e->getMessage()));
      $exception->setWrappedException($e);
      self::$lastException = $e;

      return $exception;
    }

As you can see, sfException was created mainly to display a nice debug trace
and not to replace ALL exceptions! Don’t worry to throw other exception php
provides, there’s always be a nice debug trace! ;)

PHP provides a lot of different exceptions
..........................................

PHP provides 2 predefined exceptions known as `Exception` and `ErrorException`.

`Exception` is the base class from where all other exceptions inherit from.
`ErrorException` can be used when you want that PHP throws exception instead of
reporting errors. For more information about `ErrorException`, you can read the
`dedicated documentation <http://www.php.net/manual/en/class.errorexception.php>`_.

The Standard PHP Library (SPL) provides `13 more exceptions <fr.php.net/manual/en/spl.exceptions.php>`_.
These exceptions are: `BadFunctionCallException <http://php.net/BadFunctionCallException>`_,
`BadMethodCallException <http://php.net/BadMethodCallException>`_,
`DomainException <http://php.net/DomainException>`_,
`InvalidArgumentException <http://php.net/InvalidArgumentException>`_,
`LengthException <http://php.net/LengthException>`_,
`LogicException <http://php.net/LogicException>`_,
`OutOfBoundsException <http://php.net/OutOfBoundsException>`_,
`OutOfRangeException <http://php.net/OutOfRangeException>`_,
`OverflowException <http://php.net/OverflowException>`_,
`RangeException <http://php.net/RangeException>`_,
`RuntimeException <http://php.net/RuntimeException>`_,
`UnexpectedValueException <http://php.net/UnderflowException>`_.


Each of these exception have a name that provide information on what the
problem is which is pretty useful.

Now let’s use those exceptions and see how they improve the global readability
(and scanability) of your code.

Semantic exceptions
...................

Let’s read those two pieces of code.

This one with the uncool ``sfException`` everywhere:

.. sourcecode:: php

   class Container
   {
     protected
       $maxItemCount = 2,
       $container = array();

     public function addItem($item)
     {
       if (count($this->container) < $this->maxItemCount)
       {
         $this->container[] = $item;
       }
       else
       {
         throw new sfException('Cryptic long message saying container is full');
       }
     }

     public function sliceItem()
     {
       if (empty($this->container))
       {
         throw new sfException('Cryptic long message saying container is empty');
       }

       array_slice($this->container);
     }
   }

And the cool one with semantic exceptions:

.. sourcecode:: php

    class Container
    {
      protected
        $maxItemCount = 2,
        $container = array();

      public function addItem($item)
      {
        if (count($container) < $this->maxItemCount)
        {
          $container[] = $item;
        }
        else
        {
          throw new OverflowException('Cryptic long message saying container is full');
        }
      }

      public function sliceItem()
      {
        if (empty($container))
        {
          throw new UnderflowException('Cryptic long message saying container is empty');
        }

        array_slice($container);
      }
    }

In the second example, you don’t have to read the message to know what it’s all
about. The name is sufficient. Furthermore, you’ll get more informations while
scanning the code with correct exceptions name than with sfException
everywhere.

More significative code = More readable code = More scannable code
= Happy developer = Rainbows in kittens’ eyes.

