#include <bits/stdc++.h>
using namespace std;
int main()
{
    int q;
    cin >> q;
    stack<int> st;
    while (q--)
    {
        int type;
        cin >> type;
        if (type == 1)
        {
            int x;
            cin >> x;
            st.push(x);
        }
        else
        {
            if (st.empty())
            {
                cout << 0 << endl;
                continue;
            }
            int x = st.top();
            st.pop();
            cout << x << endl;
        }
    }
}