from figure_skating import ingester

def test_no_deduction():
    ingester.read_deduction(['Deductions','0.00'])
    

def test_multiple_deduction():
    ingester.read_deduction(['Deductions','0.00'])


def test_deduction():
    ingester.read_deduction(['Deductions','0.00'])
