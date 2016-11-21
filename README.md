Wikiest - Dynamic Suggestions for Wiki pages as you type

Implementation of dynamic suggestions for top wiki pages.
As the user types the algorithm suggests the most popular
wiki pages with the specific prefix. Focus on performance
so that suggestions are speedy, but without an overuse of
RAM. The tradeoff will be a precomputed data structure on
disk that compresses title information, and uses indirect
pointers to tables that reside on disk, for navigation to
the selected wiki page.

Implemented for algorithm practice.
