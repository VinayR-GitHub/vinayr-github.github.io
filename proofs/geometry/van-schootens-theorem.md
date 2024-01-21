---
title = 'Van Schooten's Theorem'
date = 2024-01-21T15:01:04
draft = false
---

## Van Schooten's Theorem
Van Schooten's theorem is a somewhat unknown, yet elegant theorem, often employed during the solution of problems in mathematical competitions. It provides a basic statement of the relations between the lines from an equilateral triangle to its circumcircle.

## Statement
Let $ \Delta ABC $ be the equilateral triangle in Euclidean space, with circumcircle $ \omega $. Let there be a point $ P \in \omega $ such that $ d_1 , d_2 , d_3 $ are the distances $ |\overline{PA}| , |\overline{PB}| , |\overline{PC}| $, such that $ d_1 \gt d_2 \ge d_3 $. It holds that:
$$ d_1 = d_2 + d_3 $$

## Proof
Without loss of generality (WLOG), let $ P \in \widehat{AD} $ where $ D $ is the midpoint of arc $ \widehat{AB} $, and all arcs are minor. Note that $ APBC $ is incribed in $ \omega $, and hence cyclic. The remainder of the proof comes from a straight-forward application of Ptolemy's theorem:
$$ \left|\overline{BC} \right| \left|\overline{PA} \right| + \left|\overline{CA} \right| \left|\overline{PB} \right| = \left|\overline{AB} \right| \left|\overline{PC} \right| $$
$$ \left|\overline{BC} \right| d_3 + \left|\overline{CA} \right| d_2 = \left|\overline{AB} \right| d_1 $$
However, $ \left|\overline{AB} \right| = \left|\overline{BC} \right| = \left|\overline{CA} \right| $. Hence, it is trivial to show that:
$$ \therefore d_1 = d_2 + d_3 $$