# function accum($s)
# {
#     $s = ($s).ToCharArray()
#     $mumble=@()
#     $i = 1
#     foreach ($str in $s){
#         $mumble += (Get-Culture).TextInfo.ToTitleCase($str.ToString() * $i)
#         $i ++
#     }
#     $mumble -join "-"

#     return $s
# }

# $val = "abc"

# $acccum $val

function Multiply($a, $b) {
    $a * $b
  }

Multiply 4 8