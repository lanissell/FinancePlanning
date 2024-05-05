import os


def remove_test_repo(repository):
    path = repository.GetFullPath()

    if os.path.exists(path):
        os.remove(path)
