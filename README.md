# metz-pood

The Minitest API provides `assert_respond_to`, which just checks that
a ruby object can respond to a given message.

hasattr(Dynamo, key) and callable(getattr(Dynamo, key))

## 9.3

Private methods are unstable.  Avoid writing them to begin with.  Don't test
them if you can avoid it.  Consider refactoring to another object with a public
interface.  But be pragmatic and write tests for them if it turns out to be a
short term benefit.

## 9.4

When an method call on a collaborator is a query, don't test that the query
itself gets sent, simply blackbox-test the return value (or side effect) of the
method that sends the query.
