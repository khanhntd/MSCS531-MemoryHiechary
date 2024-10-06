from m5.objects.BaseTLB import BaseTLB
from m5.objects.ClockedObject import ClockedObject
from m5.params import *
from m5.proxy import *


class X86PagetableWalker(ClockedObject):
    type = "X86PagetableWalker"
    cxx_class = "gem5::X86ISA::Walker"
    cxx_header = "arch/x86/pagetable_walker.hh"

    port = RequestPort("Port for the hardware table walker")
    system = Param.System(Parent.any, "system object")
    num_squash_per_cycle = Param.Unsigned(
        4, "Number of outstanding walks that can be squashed per cycle"
    )


class X86TLB(BaseTLB):
    type = "X86TLB"
    cxx_class = "gem5::X86ISA::TLB"
    cxx_header = "arch/x86/tlb.hh"

    size = Param.Unsigned(64, "TLB size")
    system = Param.System(Parent.any, "system object")
    walker = Param.X86PagetableWalker(
        X86PagetableWalker(), "page table walker"
    )
