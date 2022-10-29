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


lld fx[]= {1,0,-1, 0,1, 1,-1,-1};
lld fy[]= {0,1,0,-1,1,-1,1,-1};
//_______________________________________________

map<string, lld > m;
string a[10000];
lld attribute[100];
lld data[10000][100];
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



void fun(string str,string egde,vector<lld> va, vector<lld> vrow)
{
    lld row=vrow.size(),n=va.size();

    lld attributeX[n],dataX[row][n];

    loopN(va.size())
    {
        attributeX[i]=attribute[va[i]];
    }

    loopN(va.size())
    {
        loopN2(vrow.size())
        {
            dataX[j][i]=data[vrow[j]][va[i]];
        }
    }





    nl;

    cout<<"__________________________________________________________________________________________________________\n";

    nl;
    loopN(va.size())
    {
        cout<<a[attributeX[i]]<<"\t\t";
    }
    nl;
    loopN(row)
    {

            loopN2(n)
            {
                cout<<a[dataX[i][j]]<<"\t\t";

            }

         nl;

    }
    nl;


    set<lld> stt;
    loopN(row)
    {
        stt.in(dataX[i][n-1]);
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
            if(dataX[i][n-1]==kkk)
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
    cout<<"H("<<a[attributeX[n-1]]<<")=";
    cout<<hfinal<<endl;


    vector< pfi >vec;
    looop(0,n-2,k)
    {


        cout<<"__________ for "<<a[attributeX[k]]<<" row ___________\n";
        //cout<<edge<<endl;
        set<lld> st;
        loopN(row)
        {
            st.in(dataX[i][k]);
        }
        llf h=0;

        for(kk:st)
        {
            //cout<<a[kk];
            nl;
            lld t=0;
            set<lld> stt;
            loopN(row)
            {
                stt.in(dataX[i][n-1]);
            }
            lld dcsn[stt.size()];
            mem(dcsn,0);


            lld idx=0;


            llf ans=0;
            loopN(row)
            {
                if(dataX[i][k]==kk)
                {
                    t++;
                    lld idx=0;
                    for(kkk:stt)
                    {
                        if(dataX[i][n-1]==kkk)
                        {
                            dcsn[idx]++;
                        }
                        idx++;

                    }

                }

            }


            cout<<"p("<<a[kk]<<")="<<t<<"/"<<row<<endl;


            idx=0;
            for(kkk:stt)
            {
                cout<<"p("<<a[kkk]<<"|"<<a[kk]<<")="<<dcsn[idx]<<"/"<<t<<endl;
                ans-=p(dcsn[idx],t);
                idx++;

            }
            cout<<"H("<<a[attributeX[n-1]]<<"|"<<a[attributeX[k]]<<")=";
            cout<<ans<<endl;

            h+=(llf)ans*((llf)t/row);
            nl;

        }
        nl;

        cout<<"H("<<a[attributeX[k]]<<")=";
        cout<<h<<endl;
        cout<<"IG("<<a[attributeX[n-1]]<<"|"<<a[attributeX[k]]<<")=";
        cout<<hfinal-h<<endl;
        vec.pb(mp((llf)hfinal-h,attributeX[k]));
        nl;
    }
    sort(all(vec));
    reverse(all(vec));


    cout<<"\t###########\t"<<str<<"---["<<egde<<"]--->"<<a[vec[0].ss]<<"    ###########"<<endl;

    lld root=-1;
    loopN(n)
    {
        if(attributeX[i]==vec[0].ss)
        {
            root=i;
            break;
        }

    }
    if(root==-1)
    {
        cout<<"\t\tERROR\n";
    }

    vector<lld>vax,vrowx;

    loopN(va.size())
    {
        if(i!=root)
        {
            vax.pb(va[i]);
        }
    }

    set<lld> sr;
    loopN(row)
    {
        sr.in(dataX[i][root]);
    }


    for(xx:sr)
    {

        set<lld>sx;

        loopN(vrow.size())
        {
            if(dataX[i][root]==xx)
            {
                sx.in(dataX[i][n-1]);
            }

        }
        if(sx.size()==1)
        {
            for(kk:sx)
            {
                cout<<"\t###########\t"<<a[vec[0].ss]<<"---["<<a[xx]<<"]--->"<<a[kk]<<"    ###########"<<endl;

            }


        }
        else if(sx.size()==0)
        {
            continue;
        }
        else
        {
            loopN(vrow.size())
            {
                if(dataX[i][root]==xx)
                {
                    vrowx.pb(vrow[i]);
                }

            }
            fun(a[vec[0].ss],a[xx],vax,vrowx);
            vrowx.clear();


        }



    }





}



void slv()
{

    fstream fin;
    fin.open ("al.txt");
    lld n;
    //cout<<"number of attribute = ";
    fin>>n;



    lld id=1;

    loopN(n)
    {
        fin>>a[id];
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
    //cout<<"number of rows = ";
    fin>>row;


    loopN(row)
    {
        loopN2(n)
        {
            fin>>a[id];

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


    vector<lld> va, vrow;
    loopN(n)
    {
        va.pb(i);
    }
    loopN(row)
    {
        vrow.pb(i);
    }
    fun("root","",va,vrow);
    va.clear();
    vrow.clear();


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
Fever  Cough  Breathing_issues  Infected
14
NO  NO  NO NO
YES  YES  YES  YES
YES  YES  NO  NO
YES  NO  YES  YES
YES  YES  YES  YES
NO  YES  NO  NO
YES  NO  YES  YES
YES  NO  YES  YES
NO  YES  YES  YES
YES  YES  NO  YES
NO  YES  NO  NO
NO  YES  YES  YES
NO  YES  YES  NO
YES  YES  NO  NO




5
outlook temp humidity windy play
14
sunny hot high False no
sunny hot high True no
overcast hot high False yes
rainy mild high False yes
rainy cool normal False yes
rainy cool normal True no
overcast cool normal True yes
sunny mild high False no
sunny cool normal False yes
rainy mild normal False yes
sunny mild normal True yes
overcast mild high True yes
overcast hot normal False yes
rainy mild high True no




3
gpa studied passed
6
L F F
L T T
M F F
M T T
H F T
H T T


*/

