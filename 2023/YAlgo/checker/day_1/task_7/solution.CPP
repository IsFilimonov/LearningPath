#include <iostream>
using namespace std;
int main ()
{
    int h1, m1, s1, h2, m2, s2, h3, m3, s3, s, s_ost, hh = 0, mm = 0, ss = 0;
    char a;
    cin >> h1 >> a >> m1 >> a >> s1;
    cin >> h2 >> a >> m2 >> a >> s2;
    cin >> h3 >> a >> m3 >> a >> s3;
    s = ((s3 - s1) + (m3 - m1)*60 + (h3 - h1)*3600)/2;
    s_ost = (23*3600+59*60+59) - (h2*3600+m2*60+s2);
    if (s > s_ost)
    {
        s -= s_ost+1;
        hh = s/3600;
        s -= hh*3600;
        mm = s/60;
        s -= mm*60;
        ss = s;
        if (mm >= 59)
        {
 
            hh += mm / 60;
            mm = mm%60;
        }
        if (ss >= 59)
        {
 
            mm += ss / 60;
            ss = ss%60;
        }
        if (hh/10 == 0)
            cout << 0 << hh << ":";
        else cout << hh << ":";
        if (mm/10 == 0)
            cout << 0 << mm << ":";
        else cout << mm << ":";
        if (ss/10 == 0)
            cout << 0 << ss;
        else cout << ss;
    }
    else
    {
        hh = s/3600 + h2;
        s -= s/3600*3600;
        mm = s/60 + m2;
        s -= s/60*60;
        ss = s + s2;
        if (mm >= 59)
        {
 
            hh += mm / 60;
            mm = mm%60;
        }
        if (ss >= 59)
        {
 
            mm += ss / 60;
            ss = ss%60;
        }
 
 
        if (hh/10 == 0)
            cout << 0 << hh << ":";
        else cout << hh << ":";
        if (mm/10 == 0)
            cout << 0 << mm << ":";
        else cout << mm << ":";
        if (ss/10 == 0)
            cout << 0 << ss;
        else cout << ss;
    }
}