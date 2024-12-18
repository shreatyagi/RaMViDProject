!
!     Enabled Extension: cuda
!     No mpif.h bindings available
!
      integer OMPI_HAVE_MPI_EXT_CUDA
      parameter (OMPI_HAVE_MPI_EXT_CUDA=0)

!
!     Enabled Extension: pcollreq
!
      integer OMPI_HAVE_MPI_EXT_PCOLLREQ
      parameter (OMPI_HAVE_MPI_EXT_PCOLLREQ=1)

      include 'openmpi/mpiext/mpiext_pcollreq_mpifh.h'

!
