from app.main import main

def test_main(capsys):
    main()
    assert 'Expense tracker' in capsys.readouterr().out
