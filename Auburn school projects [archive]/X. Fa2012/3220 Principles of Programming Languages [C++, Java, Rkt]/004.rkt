(define (unite list1 list2)
(if (null? list1)
    list2
    (if (null? list2)
        list1
        (unite (cons list1 (car list2)) (cdr list2))
        )
    )
  )