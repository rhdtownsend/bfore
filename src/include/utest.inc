! Incfile : utest
! Purpose : Support for unit testing
!
! Copyright 2024-2026 Rich Townsend
!
! This file is part of BFORE. BFORE is free software: you can
! redistribute it and/or modify it under the terms of the GNU General
! Public License as published by the Free Software Foundation, version
! 3.
!
! BFORE is distributed in the hope that it will be useful, but WITHOUT
! ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
! or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
! License for more details.
!
! You should have received a copy of the GNU General Public License
! along with this program.  If not, see <http://www.gnu.org/licenses/>.

#:include 'forum.inc'

#:def CHECK(cond, message)
   write(UNIT=OUTPUT_UNIT, FMT='(3X,A,T65)', ADVANCE='NO') ${message}$
   if (.NOT. (${cond}$)) then
      write(UNIT=OUTPUT_UNIT, FMT=*) '...FAILED'
   else
      write(UNIT=OUTPUT_UNIT, FMT=*) '...passed'
   endif
#:enddef
