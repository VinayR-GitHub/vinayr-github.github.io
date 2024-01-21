---
title = 'Cauchy-Schwarz Inequality'
date = 2024-01-19T13:22:28
draft = false
---

## The Cauchy-Schwarz Inequality
The Cauchy-Schwarz inequality is one of the most well-known and universal theorems in the history of olympiad mathematics. In its most general form, it describes the nature of arbitrary vector spaces equipped with an inner product. In this post, I will prove the case over $ \mathbb{R} $.

## Statement
Given two sequences $ (a_i)_{i \in I} \subset A \subset \mathbb{R} $ and $ (b_i)_{i \in I} \subset B \subset \mathbb{R} $ with $ I \subset \mathbb{N} $, it follows that:
$$ \left(\sum_{i = 1}^{n} {a_i^2} \right) \left(\sum_{i = 1}^{n} {b_i^2} \right) \ge \left(\sum_{i = 1}^{n} a_i b_i \right)^2 $$

## Proof
Let there exist vectors $ \vec{a} $ and $ \vec{b} $ such that:
$$ \vec{a} = \sum_{i = 1}^{n} {a_i \vec{\omega_i}} , \vec{b} = \sum_{i = 1}^{n} {b_i \vec{\omega_i}} $$
Moreover, let $ \vec{a} , \vec{b} \in \mathrm{SO} (n) $ be equipped with an inner product $ \langle \vec{v} | \vec{w} \rangle $ such that $ \langle \vec{v} | \vec{w} \rangle = \vec{v} \cdot \vec{w} $ for all $ \vec{v} , \vec{w} \in \mathrm{SO} (n) $. Let $ \vartheta $ be an arbitrary angle between $ \vec{a} , \vec{b} $. Hence, it follows that:
$$ \frac{\langle \vec{a} | \vec{b} \rangle}{|\vec{a}| |\vec{b}|} = \cos(\vartheta) $$
$$ \left| \frac{\langle \vec{a} | \vec{b} \rangle}{|\vec{a}| |\vec{b}|} \right| \le 1 $$
$$ |\langle \vec{a} | \vec{b} \rangle|^2 \le |\vec{a}|^2 |\vec{b}|^2 $$
$$ |\langle \vec{v} | \vec{w} \rangle|^2 \le \langle \vec{v} | \vec{v} \rangle \cdot \langle \vec{w} | \vec{w} \rangle $$
Therefore, the Cauchy-Schwarz inequality holds for $ \langle \vec{v} | \vec{w} \rangle = \vec{v} \cdot \vec{w} $:
$$ \therefore \left(\sum_{i = 1}^{n} {a_i^2} \right) \left(\sum_{i = 1}^{n} {b_i^2} \right) \ge \left(\sum_{i = 1}^{n} a_i b_i \right)^2 $$