inp = "ABCCBA"
length = len(inp)

for(start = 0, end =length-1 ; start != end ; start += 1, end -= 1 )
    {
        if(inp[start] == inp[end]){
            palendrome = 'Y'
    }
    else
       palendrome = 'N'
       break

    }

    if(palendrome == 'Y')
        print('String is Palendrome')
    else
        print("String is not Palendrome")