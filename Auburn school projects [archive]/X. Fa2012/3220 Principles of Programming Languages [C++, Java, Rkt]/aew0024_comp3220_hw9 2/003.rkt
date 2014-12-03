(define (append-element lst elem)
  (append lst (list elem)))

(define (reversal list)
  (if (null? list)
      '()
      (cons (reversal (cdr list)) (append '() (car list)))
      )
  )