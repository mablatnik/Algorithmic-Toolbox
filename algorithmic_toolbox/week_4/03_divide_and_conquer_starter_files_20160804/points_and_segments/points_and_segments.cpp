#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct segment
{
  int start;
  int end;
};  

vector<int> fast_count_segments(vector<pair<int,int>> &v,vector<int> points) {
  vector<int> cnt(points.size());
  //write your code here
  int n1=v.size(),n2=points.size(),i=0,j=0,k;
  for(i=0;i<n2;i++)
  {
    k=0;
    for(j=0;j<n1;j++)
    {
      if(points[i]>=v[j].first && points[i]<=v[j].second)
        k++;
      else if(points[i]<v[j].first)
        j=n1;
    }
    cnt[i] = k;
  }

  return cnt;
}

vector<int> naive_count_segments(vector<int> starts, vector<int> ends, vector<int> points) {
  vector<int> cnt(points.size());
  for (size_t i = 0; i < points.size(); i++) {
    for (size_t j = 0; j < starts.size(); j++) {  
      cnt[i] += starts[j] <= points[i] && points[i] <= ends[j];
    }
  }
  return cnt;
}

int main() {
  int n, m,a,b;
  std::cin >> n >> m;
  /*vector<int> starts(n), ends(n);
  for (size_t i = 0; i < starts.size(); i++) {
    std::cin >> starts[i] >> ends[i];
  }*/
  
  std::vector<pair<int,int>> v;
  for(auto i =0;i<n;i++)
  {
    cin>>a>>b;
    v.push_back(make_pair(a,b));
  }
  
  vector<int> points(m);
  for (auto i = 0; i < points.size(); i++) {
    std::cin >> points[i];
  }
  sort(v.begin(),v.end());
  
  //use fast_count_segments
  vector<int> cnt = fast_count_segments(v, points);
  for (size_t i = 0; i < cnt.size(); i++) {
    std::cout << cnt[i] << ' ';
  }
}
