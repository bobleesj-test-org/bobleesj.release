from bobleesj.release import new_file_2


def test_new_file():
    assert new_file_2.print_hello() == "Hello world"