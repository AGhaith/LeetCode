#include <bits/stdc++.h>
using namespace std;

bool comp(long long x, long long y)
{
    return x > y;
}

int main()
{
    long long x, y;
    cin >> x >> y;

    vector<long long> b;
    vector<long long> w;
    b.reserve(x);
    w.reserve(y);

    long long sumb = 0, sumw = 0, bc = 0, bw = 0;

    for (long long i = 0; i < x; i++)
    {
        long long temp;
        cin >> temp;
        if (temp >= 0)
        {
            sumb += temp;
            bc++;
        }
        else
        {
            b.push_back(temp);
        }
    }

    for (long long i = 0; i < y; i++)
    {
        long long temp;
        cin >> temp;
        w.push_back(temp);
    }

    sort(b.begin(), b.end(), comp);

    sort(w.begin(), w.end(), comp);

    long long j = 0;
    for (long long i = 0; i < w.size(); i++)
    {
        if (bw < bc)
        {
            if (w[i] > 0)
            {
                sumw += w[i];
                bw++;
            }
            else
            {
                break;
            }
        }
        else if (j < b.size() && w[i] > abs(b[j]))
        {
            sumw += w[i];
            sumb += b[j];
            j++;
            bw++;
            bc++;
        }
        else
        {
            break;
        }
    }

    cout << sumb + sumw;
    return 0;
}
