"""
    disc10  scheme
    date: 2021/11/02
"""

"""
    Question 4.1
    scheme define 练习
    可以在https://code.cs61a.org/中检查是否正确
"""
(define (factorial x) (if (< x 2) x (* x (factorial (- x 1)))))

"""
    Question 4.2
    使用scheme实现斐波那契函数
"""
(define (fib n) (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))

"""
    Question 5.1
    scheme list 练习
    将两个list连接在一起
"""
(define (my-append a b) (cond ((eq? a '()) b) ((eq? b '()) a)(else (cons (car a) (my-append (cdr a) b)))))

"""
    Question 5.2
    list 练习
"""
(define (find_three s) (cond ((eq? s '()) #f) ((eq? (car s) list) (find_three (car s))) ((eq? (car s) 3) #t) (else (find_three (cdr s)))))

"""
    Question 5.3
    list 练习
"""
(define (duplicate lst) (if (eq? lst '()) '() (cons (car lst) (cons (car lst) (duplicate (cdr lst))))))

"""
    Question 5.4
    list 练习
"""
(define (insert element lst index) (cond ((eq? lst '()) '()) ((< index 0) '()) ((> index 0) (insert element (cdr lst) (- index 1))) (else (cons element lst))))
