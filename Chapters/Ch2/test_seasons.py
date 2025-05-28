from Chapters.Ch2.seasons import seasons


def test_is_season_winter_output_snow():
    output = seasons('winter')
    assert output == 'Snow'


def test_is_season_fall_output_leaves():
    output = seasons('fall')
    assert output == 'Leaves'


def test_is_input_convert_to_lowercase():
    output = seasons("WinTeR")
    assert output == 'Snow'
    