#include<bits/stdc++.h>
#define lld             long long int
#define llf             long double
#define pb              push_back
#define mp              make_pair
#define in              insert
#define loopN(n)        for(lld i=0;i<n;i++)
#define loopN2(n)       for(lld j=0;j<n;j++)
#define loop(p,n)       for(lld i=p;i<=n;i++)
#define rloop(p,n)      for(lld i=n;i>=p;i--)
#define loop2(p,n)      for(lld j=p;j<=n;j++)
#define looop(p,n,i)    for(lld i=p;i<=n;i++)
#define rlooop(p,n,i)   for(lld i=n;i>=p;i--)
#define iloop(it,m)     for(it=m.begin();it!=m.end();it++)
#define all(v)          v.begin(),v.end()
#define ff              first
#define ss              second
#define INF             2e18
#define FILE            freopen("input.txt","r",stdin);freopen("output.txt","w",stdout)
#define pi              (2*acos(0.0))
#define mod             (1e9+7)
#define ISO             ios::sync_with_stdio(false);cin.tie(0)
#define mem(a,b)        memset(a,b,sizeof(a))
#define case(z)         cout<<"Case "<<z<<": "
#define setprec(a)      fixed<< setprecision(a)
#define pii	            pair<lld,lld>
#define pfi	            pair<llf,lld>
#define retdp(a)        if(a!=-1)return a

#define nl              cout<<endl

//_______________________________________________
#define on(m,p)         (m|(1<<p))
#define ison(m,p)       ((bool)(m&(1<<p)))
#define flip(m,p)       (m^(1<<p))
#define allon(p)        ((1<<p)-1)
//_______________________________________________
using namespace std;

/*
fstream fin;
    fin.open ("mytext.txt");

map< , > :: iterator it


*/
lld fx[]= {1,0,-1, 0,1, 1,-1,-1};
lld fy[]= {0,1,0,-1,1,-1,1,-1};
//_______________________________________________


llf p(lld x,lld y)
{

    llf ans=x;
    ans/=y;
    if(y==0||x==0)
    {
        return 0;
    }
    return ans*(log(ans)/log(2));
}




void slv()
{
    string a[10000];
    lld n;
    cout<<"number of attribute = ";
    cin>>n;


    map<string, lld > m;
    lld id=1;
    lld attribute[n];
    loopN(n)
    {
        cin>>a[id];
        if(m[a[id]]==0)
        {
            m[a[id]]=id;
            attribute[i]=m[a[id]];
            id++;
        }
        else
        {
            attribute[i]=m[a[id]];
        }

    }
    lld row;
    cout<<"number of rows = ";
    cin>>row;

    lld data[row][n];
    loopN(row)
    {
        loopN2(n)
        {
            cin>>a[id];

            if(m[a[id]]==0)
            {
                m[a[id]]=id;
                data[i][j]=m[a[id]];
                id++;
            }
            else
            {
                data[i][j]=m[a[id]];
            }

        }

    }
    nl;
    nl;
    loopN(row)
    {
        if(data[i][0]==m["36-55"])
        {
            loopN2(n)
            {
                //cout<<a[data[i][j]]<<"\t";

            }
            //nl;
        }


    }
    nl;


    set<lld> stt;
    loopN(row)
    {
        stt.in(data[i][n-1]);
    }
    lld dcsn[stt.size()];
    mem(dcsn,0);


    lld t=0;
    lld idx=0;
    loopN(row)
    {

        t++;
        idx=0;
        for(kkk:stt)
        {
            if(data[i][n-1]==kkk)
            {
                dcsn[idx]++;
            }
            idx++;

        }


    }
    idx=0;
    llf hfinal=0;
    for(kkk:stt)
    {
        cout<<"p("<<a[kkk]<<")="<<dcsn[idx]<<"/"<<t<<endl;
        hfinal-=p(dcsn[idx],t);
        idx++;

    }
    cout<<"H("<<a[attribute[n-1]]<<")=";
    cout<<hfinal<<endl;


    vector< pfi >vec;
    looop(0,n-2,k)
    {


        cout<<"___"<<a[attribute[k]]<<"___________\n";

        set<lld> st;
        loopN(row)
        {
            st.in(data[i][k]);
        }
        llf h=0;

        for(kk:st)
        {
            cout<<a[kk];
            nl;
            lld t=0;
            set<lld> stt;
            loopN(row)
            {
                stt.in(data[i][n-1]);
            }
            lld dcsn[stt.size()];
            mem(dcsn,0);


            lld idx=0;


            llf ans=0;
            loopN(row)
            {
                if(data[i][k]==kk) //need to apply condition
                {
                    t++;
                    lld idx=0;
                    for(kkk:stt)
                    {
                        if(data[i][n-1]==kkk)
                        {
                            dcsn[idx]++;
                        }
                        idx++;

                    }

                }

            }

            idx=0;
            for(kkk:stt)
            {
                cout<<"p("<<a[kkk]<<")="<<dcsn[idx]<<"/"<<t<<endl;
                ans-=p(dcsn[idx],t);
                idx++;

            }
            cout<<"H("<<a[attribute[n-1]]<<"|"<<a[attribute[k]]<<")=";
            cout<<ans<<endl;
            h+=(llf)ans*((llf)t/row);
            nl;

        }
        nl;

        cout<<"H("<<a[attribute[k]]<<")=";
        cout<<h<<endl;
        cout<<"IG("<<a[attribute[n-1]]<<"|"<<a[attribute[k]]<<")=";
        cout<<hfinal-h<<endl;
        vec.pb(mp((llf)hfinal-h,attribute[k]));
        nl;
    }
    sort(all(vec));
    reverse(all(vec));

    cout<<"\troot node is -> "<<a[vec[0].ss]<<endl;






}

int main()
{
    //ISO;
    lld idx=1;
    //lld t;cin>>t;while(t--)
    {
        //case(idx++);
        slv();
    }
    return 0;
}

/*

5
Age Education Income Marital_Status Buy_Computer
20
36-55   Master's        High    Single  Yes
18-35   High_School     Low     Single  No
36-55   Master's        Low     Single  Yes
18-35   Bachelor's      High    Single  No
<18     High_School     Low     Single  Yes
18-35   Bachelor's      High    Married No
36-55   Bachelor's      Low     Married No
>55     Bachelor's      High    Single  Yes
36-55   Master's        Low     Married No
>55     Master's        Low     Married Yes
36-55   Master's        High    Single  Yes
>55     Master's        High    Single  Yes
<18     High_School     High    Single  No
36-55   Master's        Low     Single  Yes
36-55   High_School     Low     Single  Yes
<18     High_School     Low     Married Yes
18-35   Bachelor's      High    Married No
>55     High_School     High    Married Yes
>55     Bachelor's      Low     Single  Yes
36-55   High_School     High    Married No







4
Education Income Marital_Status Buy_Computer
3
High_School     Low     Single  Yes
High_School     High    Single  No
High_School     Low     Married Yes





4
Education Income Marital_Status Buy_Computer
8
Master's        High    Single  Yes
Master's        Low     Single  Yes
Bachelor's      Low     Married No
Master's        Low     Married No
Master's        High    Single  Yes
Master's        Low     Single  Yes
High_School     Low     Single  Yes
High_School     High    Married No


*/

