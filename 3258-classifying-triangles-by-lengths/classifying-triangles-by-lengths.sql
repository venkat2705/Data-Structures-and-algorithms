# Write your MySQL query statement below

select 
(case when A = B and B = C then 'Equilateral' 
when C >= (A+B) or B >= (A+C) or A >= (B+C) or C < abs(A-B) or B < abs(A-C) or A < abs(B-C) then "Not A Triangle" 
when (A = B and B != C) or (A = C and A!=B) or (B=C and B!=A) then "Isosceles" 
else "Scalene" end ) as  triangle_type from triangles
