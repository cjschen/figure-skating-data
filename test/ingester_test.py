from figure_skating import ingester

def test_no_deduction():
    ingester.read_deduction(['Deductions','0.00'])
    

def test_multiple_deduction():
    ingester.read_deduction(['Deductions','Time violation:','-1.00','Falls:','-1.00(1)','-2.00'])


def test_one_deduction():
    ingester.read_deduction(['Deductions', 'Falls:','-1.00(1)','-1.00'])

def test_one_deduction():
    ingester.read_deduction(['Deductions', 'Falls:','-2.00(2)','-2.00'])
