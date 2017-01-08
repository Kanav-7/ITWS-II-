#lang racket
(provide
    vector-sum
        list-sum
        list-length
        member?
        map-sqr
        )

;;; purpose: Find sum of elements in a vector
;;; usage: (vector-sum #(-1 2 3)) => 4
;;; contract: vector? -> number?

(define vector-sum
    (lambda (v)
         (letrec ([ls-sum (lambda (ln)
                           (if (= 0 (length ln))
                                     0 (+ (first ln) (ls-sum (rest ln)))))]) (ls-sum (vector->list v)))))       

;;; purpose: Find sum of elements in a list
;;; usage: (list-sum '(1 2 3 4)) => 10
;;; contract: list? -> number? 

(define list-sum
    (lambda (ln)
          (if (= 0 (length ln))
                        0 (+ (first ln) (list-sum (rest ln))))))

;;; purpose: Find length of a list
;;; usage: (list-length '(1 2 3)) => 3
;;; contract: list? -> nat?

(define list-length
       (lambda (l)
              (if (empty? l)
                       0 (+ 1 (list-length (rest l))))))

;;; purpose: Check whether a particular value is present in a list
;;; usage: (member? '(a b c) 'a) => #t
;;; contract: list? value? -> bool?

(define member? (λ (ls x)
                  (if (empty? ls)
                      #f
                      (if (equal? (first ls) x)
                          #t
                          (member? (rest ls) x)))))


;;; purpose: To square each element in a list
;;; usage: (map-sqr '(1 2 3)) => '(1 4 9)
;;; contract: list? -> list?

(define map-sqr
      (lambda (ls)
            (if (empty? ls) empty
                       (cons (* (first ls) (first ls)) (map-sqr (rest ls))))))


