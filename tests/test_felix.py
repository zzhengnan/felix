from unittest.mock import call, patch

from felix import repeat


def test_repeat_without_args():
    @repeat
    def hello():
        print('Hey there!')

    with patch('builtins.print') as print_mock:
        hello()

    expected = [call('Hey there!')] * 2
    assert print_mock.mock_calls == expected


def test_repeat_with_default_n():
    @repeat()
    def hello():
        print('Hey there!')

    with patch('builtins.print') as print_mock:
        hello()

    expected = [call('Hey there!')] * 2
    assert print_mock.mock_calls == expected


def test_repeat_with_custom_n():
    @repeat(n=4)
    def hello():
        print('Hey there!')

    with patch('builtins.print') as print_mock:
        hello()

    expected = [call('Hey there!')] * 4
    assert print_mock.mock_calls == expected


def test_repeat_without_syntactic_sugar():
    def hello():
        print('Hey there!')

    hello = repeat(hello, n=3)
    with patch('builtins.print') as print_mock:
        hello()

    expected = [call('Hey there!')] * 3
    assert print_mock.mock_calls == expected


def test_repeat_returns_results_from_decorated_function():
    @repeat()
    def hello(name):
        return f'Hey there, {name}!'

    assert hello('Allyson') == 'Hey there, Allyson!'
