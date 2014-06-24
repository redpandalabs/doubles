from pytest import raises

from doubles import Double, expect, verify
from doubles.exceptions import MockExpectationError


class TestExpect(object):
    def test_raises_if_an_expected_method_call_is_not_made(self):
        subject = Double()

        expect(subject).to_receive('foo')

        with raises(MockExpectationError):
            verify()

    def test_passes_if_an_expected_method_call_is_made(self):
        subject = Double()

        expect(subject).to_receive('foo')

        subject.foo()

    def test_passes_if_method_is_called_with_specified_arguments(self):
        subject = Double()

        expect(subject).to_receive('foo').with_args('bar', baz='blah')

        assert subject.foo('bar', baz='blah') is None
