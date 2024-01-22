---
title = 'Jensen's Inequality with Convexity'
date = 2024-01-21T13:13:50
draft = false
---

## Jensen's Inequality with Convexity
Jensen's inequality has long remained a staple tool in the proof on inequalities, and can be applied to both olympiad and research settings. In this post, I will prove for the case of the inequality for convex functions.

## Statement
For $ \varphi $ convex in $ [a , b] $ and $ (x_i)_{i \in I} \subset [a , b] $, $ (m_i)_{i \in I} \subset \mathbb{R}^{+}$ with $ i \subset \mathbb{N} $, it follows that:
$$ \varphi \left(\frac{\sum_{i = 1}^{n} {m_i x_i}}{\sum_{i = 1}^{n} {m_i}} \right) \le \frac{\sum_{i = 1}^{n} {m_i \varphi (x_i)}}{\sum_{i = 1}^{n} {m_i}} $$

## Proof
Without loss of generality (WLOG), suppose $ \sum_{i = 1}^{n} {m_i} = 1 $. Let $ x' = \sum_{i = 1}^{n} {m_i x_i} $.
Notice that $ \phi = \varphi' $ is monotonically increasing:
$$ x_i \le x' \Rightarrow \int_{x_i}^{x'} {\phi (t) \ dt} \le \int_{x_i}^{x'} {\phi (x') \ dt} $$
$$ x_i \gt x' \Rightarrow \int_{x'}^{x_i} {\phi (t) \ dt} \ge \int_{x'}^{x_i} {\phi (x') \ dt} $$
Taking the integrals shows that:
$$ \varphi(x') - \varphi(x_i) \le \phi (x') (x' - x_i) $$
$$ m_i \varphi(x') - m_i \varphi(x_i) \le \phi (x') (m_i x' - m_i x_i) $$
$$ \varphi(x') - \sum_{i = 1}^{n} {m_i \varphi(x_i)} \le \phi (x') \left(x' - \sum_{i = 1}^{n} {m_i x_i} \right) = 0 $$
$$ \varphi(x') \le \sum_{i = 1}^{n} {m_i \varphi(x_i)} $$
The inequality follows trivially:
$$ \therefore \varphi \left(\frac{\sum_{i = 1}^{n} {m_i x_i}}{\sum_{i = 1}^{n} {m_i}} \right) \le \frac{\sum_{i = 1}^{n} {m_i \varphi (x_i)}}{\sum_{i = 1}^{n} {m_i}} $$