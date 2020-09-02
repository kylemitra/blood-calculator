
def test_HDLChecker():
    from calculator import HDLChecker
    output = HDLChecker(60)
    expected = "Normal"
    assert output == expected

    #This should fail because it should expect low
    output2 = HDLChecker(1)
    expected2 = "Normal"
    assert output2 == expected2

    output3 = HDLChecker(10)
    expected3 = "Low"
    assert output3 == expected3

    output4 = HDLChecker(50)
    expected4 = "Borderline Low"
    assert output4 == expected4
