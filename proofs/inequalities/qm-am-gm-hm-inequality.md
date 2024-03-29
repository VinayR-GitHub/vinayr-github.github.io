---
title = 'QM-AM-GM-HM Inequality'
date = 2024-01-22T15:53:42
draft = false
---

## The QM-AM-GM-HM Inequality
The QM-AM-GM-HM inequality is one of the most diversely applicable and simple inequalities to have been devised. As an essential tool in applied, research, and olympiad mathematics, it confers an elaborate way of delineating the differences between different methods used to evaluate the mean of a sequence. In this post, I will prove for the case without weights.

## The Statement
Consider a sequence of positive reals $ (x_i)_{i \in I} $ with $ I \subset \mathbb{N} $. It holds that:
$$ \sqrt{\frac{1}{n} \sum_{i = 1}^{n} {x_i^2}} \ge \frac{1}{n} \sum_{i = 1}^{n} {x_i} \ge \sqrt[n]{\prod_{i = 1}^{n} {x_i}} \ge \frac{n}{\sum_{i = 1}^{n} {\frac{1}{x_i}}} $$

## The Proof
Let us first prove for the QM-AM inequality, as below:
$$ \sqrt{\frac{1}{n} \sum_{i = 1}^{n} {x_i^2}} \ge \frac{1}{n} \sum_{i = 1}^{n} {x_i} $$
$$ \sum_{i = 1}^{n} {x_i^2} \ge \frac{1}{n} \sum_{i = 1}^{n} {x_i} \sum_{i = 1}^{n} {x_i} $$
$$ \sum_{i = 1}^{n} {n x_i^2} \ge \left(\sum_{i = 1}^{n} {x_i} \right)^2 $$
$$ \left(\sum_{i = 1}^{n} {1} \right) \left(\sum_{i = 1}^{n} {x_i^2} \right) \ge \left(\sum_{i = 1}^{n} {x_i} \right)^2 $$
This is a trivial result from the Cauchy-Schwarz inequality.
Let us then prove for the AM-GM inequality. We employ Jensen's inequality with concavity. Let $ \varphi $ be concave over $ \mathbb{R}^{+} $:
$$ \varphi \left(\frac{1}{n} \sum_{i = 1}^{n} {x_i} \right) \ge \frac{1}{n} \sum_{i = 1}^{n} {\varphi(x_i)} $$
$$ \varphi(z) \triangleq \ln(z) $$
$$ \ln \left(\frac{1}{n} \sum_{i = 1}^{n} {x_i} \right) \ge \frac{1}{n} \sum_{i = 1}^{n} {\ln(x_i)} $$
$$ \frac{1}{n} \sum_{i = 1}^{n} {x_i} \ge \exp \left(\frac{1}{n} \sum_{i = 1}^{n} {\ln(x_i)} \right) $$
$$ \frac{1}{n} \sum_{i = 1}^{n} {x_i} \ge \sqrt[n]{\prod_{i = 1}^{n} {x_i}} $$
Let us then prove for the GM-HM inequality:
$$ \sqrt[n]{\prod_{i = 1}^{n} {x_i}} \ge \frac{n}{\sum_{i = 1}^{n} {\frac{1}{x_i}}} $$
$$ \sqrt[n]{\prod_{i = 1}^{n} {\frac{1}{x_i}}} \le \frac{1}{n} \sum_{i = 1}^{n} {\frac{1}{x_i}} $$
This follows directly from the AM-GM inequality. Therefore, $ \mathrm{RMS} \ge \mathrm{AM} \ge \mathrm{GM} \ge \mathrm{HM} $:
$$ \therefore \sqrt{\frac{1}{n} \sum_{i = 1}^{n} {x_i^2}} \ge \frac{1}{n} \sum_{i = 1}^{n} {x_i} \ge \sqrt[n]{\prod_{i = 1}^{n} {x_i}} \ge \frac{n}{\sum_{i = 1}^{n} {\frac{1}{x_i}}} $$