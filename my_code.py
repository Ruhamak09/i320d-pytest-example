import pytest

def fix_phone_num(phone_num_to_fix):

  num_fix = ""
  for character in phone_num_to_fix:
    if character.isdigit():
      num_fix += character
      
  if (len(num_fix) != 10):
    raise ValueError("Can only format numbers that are exactly 10 digits long")
  
  # given "5125558823". Split the parts, then recombine and return
  area_code = num_fix[0:3] # 512 (first three digits)
  three_part = num_fix[3:6] # 555 (next three digits)
  four_part = num_fix[6:] # # 8823 (last four digits)
  
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5554429876") == '(555) 442 9876'
  assert fix_phone_num("3216543333") == '(321) 654 3333'

def test_fix_phone_num_other_formats():
  assert fix_phone_num('555-442-98761') == '(555) 442 9876'
  assert fix_phone_num('(321) 654 3333') == '(321) 654 3333'

def test_raise_value_error_for_inputs():
  with pytest.raises(ValueError):
    fix_phone_num("55544298761")
  with pytest.raises(ValueError):
    fix_phone_num("555-442-98761")
