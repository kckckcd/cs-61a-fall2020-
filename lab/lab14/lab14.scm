(define (len lst a)
  (if (eq? lst nil) a
                    (len (cdr lst) (+ a 1))
  )
)

(define (split-at lst n)
  (if (> (len lst 0) n) (if (eq? n 0) (cons nil lst) (cons (cons (car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1)))))
                         (cons lst nil)
  )
)

(define (return-back num)
        num
)

(define (compose-all funcs)
  (cond ((eq? funcs nil) return-back)
        ((eq? (cdr funcs) nil) (car funcs))
        (else (cons '(compose-all (cdr funcs)) (car funcs)))
  )
)
