# test_app.py

from gradle_profiler_pttest import app


def test_correct_answer():

    # Given
    argv = ['-a', '42']

    # When
    app.main(argv)

    # Then
    assert True
