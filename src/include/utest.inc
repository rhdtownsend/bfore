! Incfile : utest
! Purpose : Support for unit testing

#:include 'forum.inc'

#:def CHECK(cond, message)
   write(UNIT=OUTPUT_UNIT, FMT='(3X,A,T65)', ADVANCE='NO') ${message}$
   if (.NOT. (${cond}$)) then
      write(UNIT=OUTPUT_UNIT, FMT=*) '...FAILED'
   else
      write(UNIT=OUTPUT_UNIT, FMT=*) '...passed'
   endif
#:enddef
