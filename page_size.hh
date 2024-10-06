#ifndef __ARCH_X86_PAGE_SIZE_HH__
#define __ARCH_X86_PAGE_SIZE_HH__

#include "base/types.hh"

namespace gem5
{

namespace X86ISA
{
    const Addr PageShift = 12;
    const Addr PageBytes = 1ULL << PageShift;
} // namespace X86ISA
} // namespace gem5

#endif // __ARCH_X86_PAGE_SIZE_HH__
