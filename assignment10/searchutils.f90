MODULE searchutils
   
   INTERFACE linearSearchFun
      MODULE PROCEDURE linearSearch
   END INTERFACE

   INTERFACE binarySearchFun
      MODULE PROCEDURE binarySearch
   END INTERFACE

CONTAINS
        
   !  Description: Function that finds the location (idx) of a value x
   !               in an array using the linear search algorithm.
   !
   !               Find idx such that arr(idx) == x
   !
   FUNCTION linearSearch(arr, n, x) RESULT(idx)
           
           IMPLICIT NONE
   
           INTEGER, INTENT(IN) :: n      ! Number of elements in the array.
           REAL(8), INTENT(IN) :: arr(n) ! Array to search.
           REAL(8), INTENT(IN) :: x      ! Value to search for in array. 
           INTEGER :: idx    ! Result of the search. [arr(idx) == x]
           INTEGER :: i      ! Counter.

           idx = -1
           !$OMP PARALLEL DO PRIVATE(i)
           DO i = 1,n
              IF (arr(i) == x) THEN
                 idx = i
              END IF 
           END DO
           !$OMP END PARALLEL DO

   END FUNCTION linearSearch


   !  Description: Function that finds the location (idx) of a value x
   !               in a sorted array using the binary search algorithm.
   !
   !               Find idx such that arr(idx) == x
   !
   FUNCTION binarySearch(arr, n, x) RESULT(idx)

           IMPLICIT NONE
   
           INTEGER, INTENT(IN) :: n      ! Number of elements in the array.
           REAL(8), INTENT(IN) :: arr(n) ! Array to search.
           REAL(8), INTENT(IN) :: x      ! Value to search for in array. 
           INTEGER :: idx    ! Result of the search. [arr(idx) == x]
           INTEGER :: s      ! Start of the array index.
           INTEGER :: e      ! End of the array index.
           INTEGER :: mid    ! Midpoint index.

           idx = -1
           s = 1
           e = n

           DO WHILE (s <= e)
             
              mid = s + (e - s) / 2

              IF (arr(mid) == x) THEN
                 idx = mid
                 EXIT 

              ELSE IF (arr(mid) < x) THEN
                 s = mid + 1

              ELSE
                 e = mid - 1     

              END IF
              
           END DO

   END FUNCTION binarySearch

END MODULE searchutils
