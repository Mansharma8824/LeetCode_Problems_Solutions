bool isPalindrome(int x) {
    int rev = 0;
    int origenal = x;
    if (x < 0)
    {
        return false;
    }
    while (x > 0)
    {
        int rem = x%10;
        if (rev > (INT_MAX - rem) / 10)
        {
            return false;
        }
        rev = rev *10 + rem;
        x = x/10;
    }
    if (rev == origenal){
        return true;
    }
    else
    {
        return false;
    }


    
}