#include <bits/stdc++.h>
using namespace std;
int main()
{
    // first = val
    // second = how many
    int n;
    cin >> n;
    vector<pair<int, int>> v(n);
    while (n--)
    {

        int temp;
        cin >> temp;
        int val = 1;
        if (temp == v.back().first)
        {
            int val = v.back().second + 1;
            if (val == 3)
            {
                cout << "Yes" << endl;
                return 0;
            }
            v.push_back({temp, val});
        }
        else
        {
            v.push_back({temp, val});
        }
    }
    cout << "No" << endl;
}