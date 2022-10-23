CONTENT = "content"

def test_create_file(tmp_path):
    # tmp_path is pathlib.Path obj
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1

# tmp_path
# tmp_path_factory
# tmpdir
# tmpdir_factory
