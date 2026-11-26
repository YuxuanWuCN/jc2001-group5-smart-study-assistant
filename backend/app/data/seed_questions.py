"""
StudyGraph (JC2001 Group 5) - Curated Multi-Discipline Seed Question Bank
Contains 17 curated questions across 9 subjects (law, cs, econ, se, or, mis, prob_stat, mkt, eng)
with 51 fine-grained distractor traps.
"""

from typing import List, Dict
from backend.app.models.quiz import (
    QuizItem,
    OptionItem,
    TrapDetail,
    GraphNode,
    GraphEdge,
    GraphData
)

SEED_QUESTIONS: List[QuizItem] = [
    # =========================================================================
    # 1. LAW (Civil and Commercial Law · Civil Code)
    # =========================================================================
    QuizItem(
        id="law_1",
        subject="law",
        difficulty="★★★☆☆",
        tag="Revocable juristic acts · duration of the right of revocation",
        stem="On 1 March 2023, Party A was induced by fraud to conclude a second-hand car sale contract with Party B, and on 1 May of the same year Party A became aware of the fraud. Under the Civil Code provisions on revocable juristic acts, from what date does the preclusive period for Party A to request a people's court to rescind the contract start to run, and by what date must it expire at the latest?",
        options=[
            OptionItem(key="A", text="Runs from the date the contract was signed (1 March 2023) and expires no later than 3 years afterwards", is_correct=False, trap_id="trap_law_1"),
            OptionItem(key="B", text="Runs from the date the fraud became known (1 May 2023) and expires no later than 1 year afterwards", is_correct=True),
            OptionItem(key="C", text="Runs from the date the fraudulent conduct ceased and expires no later than 1 year afterwards", is_correct=False, trap_id="trap_law_2"),
            OptionItem(key="D", text="Runs from the date the contract was signed and, irrespective of knowledge, expires in all cases within 2 years", is_correct=False, trap_id="trap_law_3"),
        ],
        explanation="[Authoritative examination analysis · Civil Code Art. 152]: The right of revocation for material misunderstanding must be exercised within 90 days of the date it becomes known, and the right of revocation for fraud must be exercised within 1 year of the date the fraud is known or ought to have been known; the right of revocation is extinguished if it is not exercised within 5 years of the date of the act. This period is preclusive in nature: it is not subject to suspension, interruption or extension!",
        traps={
            "trap_law_1": TrapDetail(
                title="🚨 Classic confusion: applying the 3-year limitation period to a formative right",
                desc="The most common trap in the cohort. General-purpose chatbots also tend to apply the 3-year limitation period of Civil Code Art. 188 to the right of revocation. A limitation period governs claims, whereas the right of revocation is a formative right and is therefore subject to a strict statutory preclusive period.",
                prereq="Prerequisite: the distinction between claims and formative rights, and statutory preclusive periods",
                radar_hit="trapDefense"
            ),
            "trap_law_2": TrapDetail(
                title="🚨 Norm-mismatch trap: conflating the statutory start dates for 'fraud' and 'duress'",
                desc="The Civil Code draws a strict distinction between fraud and duress: only duress runs from 'the date the duress ceased', whereas fraud runs from 'the date the ground for revocation is known or ought to have been known'!",
                prereq="Prerequisite: statutory start-date conditions for defects of will caused by duress and fraud",
                radar_hit="boundary"
            ),
            "trap_law_3": TrapDetail(
                title="🚨 Repealed-provision rote-memorisation trap: confusing the old Contract Law with the current Civil Code",
                desc="The student wrongly applies a provision of the repealed Contract Law. The current Civil Code uniformly provides a 1-year period running from fraud and a maximum protection period of 5 years (not 2 years).",
                prereq="Prerequisite: the system of the right of revocation in the General Provisions of the Civil Code",
                radar_hit="recall"
            )
        },
        graph=GraphData(
            title="Civil Code Art. 152 · topology subgraph of revocable juristic acts",
            nodes=[
                GraphNode(id="c1", label="Preclusive period of the right of revocation", type="core", x=260, y=140),
                GraphNode(id="p1", label="1 year from knowledge of the fraud", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Maximum 5 years from the act", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: misapplying the 3-year limitation period", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: misremembering the duress end point", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Primary preclusive period"),
                GraphEdge(from_node="p2", to_node="c1", label="Maximum protection period"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (confusing the nature of the right)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (mismatching the start date)"),
            ]
        ),
        socratic_prompt="Stop and think for a moment: in civil-law theory, when a party extinguishes an already-formed contract, is it exercising a 'claim' that compels the counterparty to pay money or return goods, or a 'formative right' that can alter the legal relationship by unilateral declaration? Why are the time limits for these two kinds of right fundamentally different?"
    ),

    QuizItem(
        id="law_2",
        subject="law",
        difficulty="★★★★☆",
        tag="Property law · requirements and defences of bona fide acquisition of movables",
        stem="A lends his professional DSLR camera to B for use. Without authorisation, B sells it at the fair market price of RMB 12,000 to C, a photography enthusiast who is unaware of the arrangement, and completes delivery and payment on the spot. A week later A discovers this and asserts ownership against C, demanding the camera's return without compensation. As to the legal effect of this case, which of the following statements is entirely correct?",
        options=[
            OptionItem(key="A", text="Because B had no power of disposal over the camera, the sale contract between B and C is absolutely void ab initio and C cannot acquire ownership", is_correct=False, trap_id="trap_law_2_1"),
            OptionItem(key="B", text="C has acquired original ownership of the camera under the bona fide acquisition regime of the Civil Code, and A has no right to demand return of the original property", is_correct=True),
            OptionItem(key="C", text="Because the camera was lent rather than lost, C must first pay A reasonable compensation before retaining it", is_correct=False, trap_id="trap_law_2_2"),
            OptionItem(key="D", text="Bona fide acquisition applies only to real-property rights; a movable remains in a pending-validity state until the original owner A expressly ratifies the transfer", is_correct=False, trap_id="trap_law_2_3"),
        ],
        explanation="[Authoritative examination analysis · Civil Code Arts. 311 and 597]: (1) A sale contract concluded by a person without power of disposal is valid (the old Contract Law Art. 51 pending-validity doctrine is entirely abolished); (2) the requirements for bona fide acquisition are: the transferee is in good faith and free of gross negligence at the time of transfer, the transfer is at a reasonable price, and delivery has been completed in accordance with law. C satisfies all three requirements and therefore acquires ownership of the movable by operation of law; A may only claim tort damages or unjust enrichment from B, the person without power of disposal!",
        traps={
            "trap_law_2_1": TrapDetail(
                title="🚨 Repealed-law rote-memorisation trap: equating a 'defect in the power of disposal' with an 'absolutely void sale contract'",
                desc="This is the classic disaster zone that 58% of students fall into in law-school finals and postgraduate entrance examinations! The Civil Code clearly separates the obligational act (the contractual claim) from the act of disposal (the change in real rights). A sale contract remains valid even if concluded without power of disposal; failure to perform gives rise to liability for breach, and a bona fide transferee is directly protected by bona fide acquisition!",
                prereq="Prerequisite: the separation principle between the validity of a contractual claim and the change of real rights",
                radar_hit="recall"
            ),
            "trap_law_2_2": TrapDetail(
                title="🚨 Rule-confusion trap: applying the 'redemption of lost or stolen property' rule to a voluntarily lent, entrusted article",
                desc="Civil Code Art. 312 provides a 2-year right to demand return upon payment of consideration only for lost property and other 'things that left possession without the true owner's intent'. Here A voluntarily lent the camera to B (an article entrusted to possession), so the original owner must bear the trust risk himself; there is simply no right of redemption for consideration!",
                prereq="Prerequisite: the difference in legal consequences between lost or escaped articles and entrusted articles",
                radar_hit="boundary"
            ),
            "trap_law_2_3": TrapDetail(
                title="🚨 Blind spot in the scope of the doctrine: bona fide acquisition spans both movables and immovables",
                desc="General-purpose AI frequently mixes up delivery for movables with registration for immovables. Bona fide acquisition is precisely a statutory regime of original acquisition resting on two pillars: the public credibility of possession for movables and of registration for immovables!",
                prereq="Prerequisite: the principles of publicity and public credibility as applied to movables",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Civil Code Art. 311 · topology of the elements and defences of bona fide acquisition",
            nodes=[
                GraphNode(id="c1", label="Bona fide acquisition of movables (Art. 311)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Good faith + reasonable price + completed delivery", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Risk allocation for entrusted articles", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: wrongly treating the sale contract as void", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: misapplying lost-property redemption", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Three statutory elements"),
                GraphEdge(from_node="p2", to_node="c1", label="Bars return of the original"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (failing to distinguish obligational from dispositive acts)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (conflating escaped and entrusted articles)"),
            ]
        ),
        socratic_prompt="Think about this: if the original owner A carelessly lent the camera to an unreliable friend B, while the bona fide buyer C paid real money in the open market and obtained the camera, why does the law protect C rather than A? What commercial-transaction-security value orientation does this reflect?"
    ),

    QuizItem(
        id="law_3",
        subject="law",
        difficulty="★★★★☆",
        tag="General Provisions · apparent authority and liability based on appearance",
        stem="A software technology company dismissed its vice-president of sales, Zhang, but negligently failed to collect in time the blank business authorisation letter bearing the company seal and the dedicated contract seal that he held. The next day Zhang, using those documents and acting in the company's name, concluded an RMB 800,000 server-room leasing contract with a cloud service provider that was unaware of his departure and had exercised ordinary care. As to the validity of, and liability under, that contract, which of the following statements is correct?",
        options=[
            OptionItem(key="A", text="Zhang had no authority after leaving office, so the contract is absolutely void ab initio and the technology company bears no civil liability whatsoever", is_correct=False, trap_id="trap_law_3_1"),
            OptionItem(key="B", text="Apparent authority is established; the contract is valid as against the technology company, which must bear the contractual obligation to perform and pay", is_correct=True),
            OptionItem(key="C", text="The contract is a pending-validity contract; if the technology company does not ratify it within the statutory 30 days, the contract is extinguished outright", is_correct=False, trap_id="trap_law_3_2"),
            OptionItem(key="D", text="Apparent authority can be established only if the cloud service provider can fully prove that the technology company's executives had a subjective intent to defraud", is_correct=False, trap_id="trap_law_3_3"),
        ],
        explanation="[Authoritative examination analysis · Civil Code Art. 172]: Where an actor performs an agency act without authority, beyond the scope of authority, or after the authority has terminated, and the counterparty has reason to believe that the actor has authority, the agency act is valid. The company's failure to recover the seals and the authorisation letter amounts to gross negligence (an attributable appearance), and the counterparty is in good faith and free from negligence, so apparent authority is established! After performing, the company may seek recourse against Zhang!",
        traps={
            "trap_law_3_1": TrapDetail(
                title="🚨 Mechanical denial-of-authority trap: ignoring the commercial-appearance doctrine's tilt towards bona fide third parties",
                desc="Many beginners see only the half-sentence 'Zhang had left office and had no authority' and mechanically hold the contract void. The very purpose of the apparent-authority regime is to bind the principal to the legal consequences when authority is substantively lacking but the principal has created an appearance of right!",
                prereq="Prerequisite: the appearance-of-right theory and the protection of reliance interests",
                radar_hit="trapDefense"
            ),
            "trap_law_3_2": TrapDetail(
                title="🚨 Reversed-order trap: downgrading 'apparent authority' to the 'pending validity of unauthorised agency in the narrow sense'",
                desc="Once apparent authority is established, the counterparty has a choice: it may either assert that the apparent agency is valid and require the company to perform, or it may rescind on its own initiative. But the principal (the technology company) has no right at all to annul the contract unilaterally by 'refusing to ratify'!",
                prereq="Prerequisite: the breakpoint in legal consequences between apparent authority and unauthorised agency in the narrow sense",
                radar_hit="boundary"
            ),
            "trap_law_3_3": TrapDetail(
                title="🚨 Over-strict attribution trap: confusing 'attributability of the appearance of right' with 'intent to commit a tort'",
                desc="Establishing apparent authority does not require the principal to have any subjective intent to defraud! Objective negligence such as poor seal management or failure to recover the authorisation letter, if it creates the appearance of right, is sufficient to establish the principal's attributability!",
                prereq="Prerequisite: the criteria for the objective and subjective elements of apparent authority",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="Civil Code Art. 172 · topology of the attribution of apparent-authority effects",
            nodes=[
                GraphNode(id="c1", label="Apparent authority (Art. 172)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Appearance of right + principal's negligence", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Counterparty in good faith and without negligence", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: wrongly held absolutely void", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: wrongly requiring the principal's intent", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Appearance creates attributability"),
                GraphEdge(from_node="p2", to_node="c1", label="Reliance-protection element"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (mechanical view of lack of authority)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (over-strict subjective element)"),
            ]
        ),
        socratic_prompt="Put yourself in the shoes of a supplier: if the person in front of you produces an authorisation letter and company seal stamped with the official red seal, could you realistically check whether that company issued an internal notice dismissing him today? Why does the law make a company that manages its seals carelessly foot the bill?"
    ),

    # =========================================================================
    # 2. CS (Computer Architecture)
    # =========================================================================
    QuizItem(
        id="cs_1",
        subject="cs",
        difficulty="★★★★☆",
        tag="Classic RISC pipeline · hazard handling and forwarding bypass",
        stem="In a standard five-stage in-order pipeline (IF, ID, EX, MEM, WB), instruction i is an arithmetic operation (e.g. add R1, R2, R3), and the immediately following instruction i+1 (e.g. sub R4, R1, R5) needs R1 in its execute stage. Regarding the pipeline hazard and its optimisation in this scenario, which of the following statements is correct?",
        options=[
            OptionItem(key="A", text="This is a write-after-read (WAR) anti-dependence hazard; the five-stage pipeline must insert 2 stall cycles", is_correct=False, trap_id="trap_cs_1"),
            OptionItem(key="B", text="This is a read-after-write (RAW) true data dependence; hardware forwarding can eliminate all stalls", is_correct=True),
            OptionItem(key="C", text="This is a structural hazard; it must be solved by upgrading the single-port register file to a multi-port one", is_correct=False, trap_id="trap_cs_2"),
            OptionItem(key="D", text="This is a control hazard; a branch history table (BHT) must be introduced to predict execution", is_correct=False, trap_id="trap_cs_3"),
        ],
        explanation="[Authoritative examination analysis · data forwarding in the classic RISC five-stage pipeline]: By the end of its EX stage (at the ALU output) instruction i has already computed the new value of R1, whereas instruction i+1 needs R1 only at the start of its EX stage. By routing a forwarding path out of the EX/MEM pipeline register into the ALU inputs, bubbles can be eliminated entirely (zero stall)!",
        traps={
            "trap_cs_1": TrapDetail(
                title="🚨 Advanced-concept rote-memorisation trap: WAR/WAW anti-dependences cannot occur in an in-order five-stage pipeline at all!",
                desc="This is a knowledge hallucination that general-purpose LLMs produce very easily! WAR hazards can arise only in superscalar processors that support out-of-order execution (e.g. the Tomasulo architecture). In the classic five-stage in-order pipeline instructions flow in program order, so an earlier instruction can never read a register after a later one!",
                prereq="Prerequisite: the difference in premises between in-order and out-of-order execution",
                radar_hit="boundary"
            ),
            "trap_cs_2": TrapDetail(
                title="🚨 Classification-confusion trap: mistaking 'register data transfer' for a 'hardware structural resource conflict'",
                desc="A structural hazard means several instructions contending for the same physical component in the same clock cycle (for example, a single-port memory being read for an instruction and for data at once). The stem clearly describes a forward-backward dependence on a register value, which is a pure data hazard!",
                prereq="Prerequisite: the boundaries between the three pipeline hazard classes",
                radar_hit="recall"
            ),
            "trap_cs_3": TrapDetail(
                title="🚨 Over-generalisation trap: arithmetic instructions contain no conditional branch",
                desc="Control hazards are caused only by conditional branches (beq, bne) or unconditional jumps (jmp) modifying the PC; ordinary arithmetic instructions have no branch-prediction requirement at all!",
                prereq="Prerequisite: control hazards and the semantics of branch instructions",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="RISC five-stage pipeline · data dependence and forwarding-path map",
            nodes=[
                GraphNode(id="c1", label="Pipeline data hazard (RAW)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Premise: in-order issue and execution", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Solution: ALU forwarding path", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Hallucination trap: misapplying WAR anti-dependence", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Confusion trap: wrongly judged as structural contention", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Microarchitectural constraint"),
                GraphEdge(from_node="p2", to_node="c1", label="Zero-stall hardware optimisation"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (conflating out-of-order and in-order concepts)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (conflating resource contention and data flow)"),
            ]
        ),
        socratic_prompt="Examine the space-time diagram of the MIPS five-stage pipeline: with in-order issue, if an instruction has already obtained its arithmetic result at the end of clock cycle 3, while the next instruction needs that result only at the start of cycle 4, why should we wait needlessly until cycle 5 when the result is written back to the register file? Could we build a short cut in between?"
    ),

    QuizItem(
        id="cs_2",
        subject="cs",
        difficulty="★★★★☆",
        tag="Memory hierarchy · set-associative cache mapping and miss analysis",
        stem="A 32-bit byte-addressed processor has a 32KB data cache with a block size of 64 bytes and 4-way set-associative mapping. A program now repeatedly loops over a large array with a stride of 32KB, causing severe conflict misses. Regarding the cache field breakdown and miss optimisation, which of the following statements is entirely correct?",
        options=[
            OptionItem(key="A", text="The main-memory address is split as Tag = 19 bits, Index = 7 bits, Offset = 6 bits; raising associativity to 8 ways directly alleviates the conflict misses", is_correct=True),
            OptionItem(key="B", text="The main-memory address is split as Tag = 18 bits, Index = 8 bits, Offset = 6 bits; changing the replacement policy from LRU to FIFO reduces the miss rate", is_correct=False, trap_id="trap_cs_2_1"),
            OptionItem(key="C", text="The main-memory address is split as Tag = 20 bits, Index = 6 bits, Offset = 6 bits; increasing the block size from 64B to 128B cures the conflict misses", is_correct=False, trap_id="trap_cs_2_2"),
            OptionItem(key="D", text="Adding a single instruction prefetch buffer inside the CPU eliminates all data-cache misses completely", is_correct=False, trap_id="trap_cs_2_3"),
        ],
        explanation="[Authoritative examination analysis · cache address breakdown and 3C misses]: (1) block size 64B = 2⁶, so Offset = 6 bits; total blocks = 32KB / 64B = 512 blocks; with 4-way set associativity the number of sets = 512 / 4 = 128 sets = 2⁷, so Index = 7 bits; Tag = 32 - 7 - 6 = 19 bits! (2) Conflict misses arise because several data items map to the same index set; increasing the number of ways (for example to 8 ways) or introducing a victim cache are the classic effective remedies!",
        traps={
            "trap_cs_2_1": TrapDetail(
                title="🚨 Double trap in set counting and replacement policy: confusing total cache blocks with the number of sets",
                desc="Many students treat the 512 blocks directly as 512 sets and therefore derive a 9-bit or 8-bit Index. Worse still, LRU, grounded in temporal locality, is the best theoretical and engineering baseline; FIFO not only yields a higher miss rate but also triggers the famous Belady anomaly!",
                prereq="Prerequisite: the set-count formula for set-associative caches and the principle of locality",
                radar_hit="precision"
            ),
            "trap_cs_2_2": TrapDetail(
                title="🚨 Blind block-size increase trap: an oversized block compresses the number of sets and aggravates conflict misses",
                desc="With total cache capacity fixed, blindly increasing the block size sharply halves the number of sets, which makes stride-access conflict misses even worse and significantly raises the main-memory miss penalty!",
                prereq="Prerequisite: the trade-off structure of the 3C miss model (compulsory / capacity / conflict)",
                radar_hit="boundary"
            ),
            "trap_cs_2_3": TrapDetail(
                title="🚨 Component-role mismatch trap: conflating instruction prefetch with data memory access",
                desc="An instruction prefetch buffer performs adaptive fetching of a sequential instruction stream; it cannot reduce conflict misses in data-intensive array reads and writes that jump randomly with a large stride!",
                prereq="Prerequisite: the decoupling of instruction-cache and data-cache behaviour under the Harvard architecture",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="Set-associative cache · address decoding and conflict-miss trade-off map",
            nodes=[
                GraphNode(id="c1", label="4-way set associative (Index 7 bits)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Block size 64B (Offset 6 bits)", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Capacity 32KB (128 sets / Tag 19 bits)", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: mistaking block count for set count", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: wrongly assuming FIFO beats LRU", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Low-order in-block addressing"),
                GraphEdge(from_node="p2", to_node="c1", label="Associativity and set-count constraint"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (forgetting to divide by the number of ways)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (violating locality in the replacement policy)"),
            ]
        ),
        socratic_prompt="Take out some paper and calculate: if a reservoir has 512 tanks, each individually numbered, and we now group every 4 tanks into one large group, how many large groups are there in total? Why does the addressing hardware need to decode only the group number, while the 4 tanks within a group have their tags compared in parallel?"
    ),

    QuizItem(
        id="cs_3",
        subject="cs",
        difficulty="★★★★★",
        tag="Virtual memory system · TLB and page-fault handling sequence",
        stem="In a virtual-memory system supporting modern multi-level page tables, when the CPU executes a load/store instruction (e.g. lw $t0, 0($a0)) and address translation occurs, which of the following statements about the timing and hardware cooperation among the TLB, the page table and page faults is entirely correct?",
        options=[
            OptionItem(key="A", text="On a TLB hit the CPU obtains the physical address directly and issues the memory read, with no need whatsoever to access the multi-level page table in main memory", is_correct=True),
            OptionItem(key="B", text="On a TLB miss the MMU hardware must immediately report a page-fault exception to the OS kernel and suspend the current process", is_correct=False, trap_id="trap_cs_3_1"),
            OptionItem(key="C", text="After the OS page-fault handler has completed the transfer from disk, the CPU resumes execution at the 'next instruction (PC+4)' after the faulting one", is_correct=False, trap_id="trap_cs_3_2"),
            OptionItem(key="D", text="When the valid bit in the page table is 1 and the TLB misses, the physical page must already have been fully swapped out to the disk swap area", is_correct=False, trap_id="trap_cs_3_3"),
        ],
        explanation="[Authoritative examination analysis · the virtual-address translation pipeline]: (1) The TLB is a cache of page-table entries; on a TLB hit the VA-to-PA translation completes within 1 cycle; (2) a TLB miss is not the same as a page fault! The hardware page walker automatically traverses the main-memory page table, and if the PTE has Valid = 1 it merely needs to refill the TLB with that entry, with no need to wake the OS fault handler at all; (3) a page fault is a fault-class exception, so after the page has been brought in the hardware must re-execute the original instruction that raised the exception!",
        traps={
            "trap_cs_3_1": TrapDetail(
                title="🚨 Classic high-risk confusion trap: mistaking a 'TLB miss' for a 'page fault'",
                desc="This is the core pitfall that LLMs across the web answer wrongly and that 71% of students get wrong in finals! A TLB miss merely means the TLB has not cached that page-table entry; the physical page may well be sitting safely in physical memory. A real page fault is triggered only when the page-table lookup finds Valid = 0 (the page has not yet been loaded into memory)!",
                prereq="Prerequisite: the TLB caching mechanism versus the semantics of the page-table valid bit",
                radar_hit="trapDefense"
            ),
            "trap_cs_3_2": TrapDetail(
                title="🚨 Exception-return semantics trap: applying the 'interrupt returns to PC+4' rule to a 'fault re-executes the instruction'",
                desc="An interrupt is asynchronous and normally returns to the next instruction; a page fault, however, is a fault, and the load/store instruction has not yet successfully read its data. Jumping straight to the next instruction would load garbage into the destination register and the program logic would collapse!",
                prereq="Prerequisite: the PC-saving conventions of the three exception classes (interrupt, trap, fault)",
                radar_hit="boundary"
            ),
            "trap_cs_3_3": TrapDetail(
                title="🚨 Fully inverted flag-logic trap: Valid = 1 actually means the page is in physical memory",
                desc="A valid/present bit of 1 means the page is in a physical frame in main memory; only 0 means the page is unallocated or has been swapped out to the disk swap area!",
                prereq="Prerequisite: the PTE structure (valid, dirty, reference bits)",
                radar_hit="recall"
            )
        },
        graph=GraphData(
            title="Virtual memory · topology of TLB lookup and page-fault handling",
            nodes=[
                GraphNode(id="c1", label="VA address-translation pipeline", type="core", x=260, y=140),
                GraphNode(id="p1", label="TLB hit: PA in 1 cycle", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="TLB miss ≠ page fault (page walk)", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Hallucination trap: TLB miss reported as page fault", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: page fault returns to PC+4", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Hit fast path"),
                GraphEdge(from_node="p2", to_node="c1", label="Automatic hardware refill"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (not distinguishing TLB from page-table levels)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (conflating fault and interrupt returns)"),
            ]
        ),
        socratic_prompt="Think back: if a librarian has an excellent memory (the TLB) but cannot recall which shelf a particular book is on (a TLB miss), does that necessarily mean the book has been discarded or borrowed? Could he simply consult the master catalogue cards (the page table) and find it?"
    ),

    # =========================================================================
    # 3. ECON (Econometrics)
    # =========================================================================
    QuizItem(
        id="econ_1",
        subject="econ",
        difficulty="★★★★☆",
        tag="Violation of classic assumptions · multicollinearity and omitted-variable bias",
        stem="In the multiple regression model Y = β₀ + β₁X₁ + β₂X₂ + u, suppose there is severe but not perfect multicollinearity between the regressors X₁ and X₂. Which of the following descriptions of the properties of the ordinary least squares (OLS) estimator is entirely correct?",
        options=[
            OptionItem(key="A", text="The OLS estimator loses unbiasedness, produces severe endogeneity bias and cannot objectively reflect the true population parameters", is_correct=False, trap_id="trap_econ_1"),
            OptionItem(key="B", text="The Gauss-Markov theorem fails entirely and the OLS estimator is no longer the best linear unbiased estimator (BLUE)", is_correct=False, trap_id="trap_econ_2"),
            OptionItem(key="C", text="The OLS estimator remains unbiased and BLUE, but the parameter variances are inflated, which undermines the t-tests", is_correct=True),
            OptionItem(key="D", text="The model's overall coefficient of determination R² collapses to near 0", is_correct=False, trap_id="trap_econ_3"),
        ],
        explanation="[Authoritative examination analysis · the statistical consequences of multicollinearity]: Under the strict exogeneity assumption E(u|X)=0 and the homoskedasticity assumption, provided there is no 'perfect collinearity' (|X'X| ≠ 0) the Gauss-Markov theorem holds in full! OLS remains unbiased and BLUE! The real consequence of collinearity is that the variance inflation factor (VIF) soars, standard errors become too large and the t statistic of each individual variable falls substantially, while the overall regression's F test and R² usually remain high!",
        traps={
            "trap_econ_1": TrapDetail(
                title="🚨 Confusing the boundary between unbiasedness and efficiency: equating 'insufficient estimation precision' with a 'biased estimator'",
                desc="Many students, and general-purpose LLMs unconstrained by graph facts, answer 'the estimator is biased' at once! Bias arises only when a key variable is omitted or endogeneity is present. Correlation among regressors never destroys unbiasedness!",
                prereq="Omitted-variable bias and the Gauss-Markov theorem: the premise E(u|X)=0 required by the mathematical proof of unbiasedness",
                radar_hit="recall"
            ),
            "trap_econ_2": TrapDetail(
                title="🚨 Misreading the theorem's conditions trap: wrongly concluding that the BLUE property fails",
                desc="Among all linear unbiased estimators OLS still has the smallest variance (it is BLUE); it is merely that this 'minimum variance' has itself been pushed up by the sample data.",
                prereq="Prerequisite: the boundaries of the Gauss-Markov theorem's proof",
                radar_hit="boundary"
            ),
            "trap_econ_3": TrapDetail(
                title="🚨 Classic counter-intuitive symptom trap: under collinearity R² and F are often spuriously high!",
                desc="The most classic textbook symptom of multicollinearity is: the F test is highly significant and R² is high (e.g. 0.85), yet the t test of every individual regressor fails to reject the null hypothesis!",
                prereq="Prerequisite: the difference between the joint-hypothesis F test and the individual t test",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="Multicollinearity · topology of its statistical properties and diagnostic traps",
            nodes=[
                GraphNode(id="c1", label="Multicollinearity", type="core", x=260, y=140),
                GraphNode(id="p1", label="Assumption holds: E(u|X)=0 (strict exogeneity)", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Property: still BLUE (unbiased and efficient)", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Hallucination trap: wrongly judged as endogeneity bias", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Symptom trap: wrongly expecting R² to collapse", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Premise guaranteeing unbiasedness"),
                GraphEdge(from_node="p2", to_node="c1", label="Minimum-variance property"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (conflating bias with high variance)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (ignoring the overall F test)"),
            ]
        ),
        socratic_prompt="Think: what is the key assumption in the Gauss-Markov theorem that guarantees OLS unbiasedness? If an omitted variable enters the error term, are the regressors still orthogonal to the error term? Does the expected value of the parameter estimate equal the true population parameter?"
    ),

    QuizItem(
        id="econ_2",
        subject="econ",
        difficulty="★★★★★",
        tag="Core of causal inference · instrumental variables (IV/2SLS) and weak instruments",
        stem="In estimating the causal effect of years of education (Educ) on log wages (ln(Wage)), the explanatory variable Educ is severely endogenous because of an unobservable omitted factor, 'individual innate ability'. The researcher selects 'the distance in kilometres from the student's family home to the nearest university (Distance)' as a candidate instrument Z. Which of the following statements about instrument validity and the properties of two-stage least squares (2SLS) is entirely correct?",
        options=[
            OptionItem(key="A", text="Z must satisfy both the relevance condition (Cov(Z, Educ) ≠ 0) and the strict exogeneity/exclusion assumption (Cov(Z, u) = 0 and Z must not directly determine wages)", is_correct=True),
            OptionItem(key="B", text="Even if the first-stage regression's F statistic is only 2.8 (far below 10), the 2SLS estimator remains absolutely unbiased with minimum variance as long as the sample size N tends to infinity", is_correct=False, trap_id="trap_econ_2_1"),
            OptionItem(key="C", text="When the model is exactly identified (number of endogenous variables = number of instruments = 1), a Sargan-Hansen over-identification test can be used to test statistically and rigorously whether Z is exogenous", is_correct=False, trap_id="trap_econ_2_2"),
            OptionItem(key="D", text="To strengthen the causal interpretation, a valid instrument Z must have a significant and directly strong driving correlation with the dependent variable ln(Wage)", is_correct=False, trap_id="trap_econ_2_3"),
        ],
        explanation="[Authoritative examination analysis · instrumental variables and causal identification]: (1) The two iron laws of an instrument: the exogeneity condition (orthogonal to the disturbance and with no direct causal path) plus the relevance condition (strongly correlated with the endogenous variable); (2) the Staiger-Stock rule of thumb: only a first-stage F > 10 rules out the weak-instrument risk! A weak instrument can make 2SLS even more biased than ordinary OLS! (3) Under exact identification the model has 0 degrees of freedom, so the exogeneity assumption must rest on economic-theoretic argument and cannot be tested directly by mathematical means!",
        traps={
            "trap_econ_2_1": TrapDetail(
                title="🚨 Fatal blind spot on weak instruments: a large sample does not automatically rescue the severe bias of a weak instrument",
                desc="This is the top-tier empirical disaster scene in econometrics! When first-stage relevance is weak (F < 10), the asymptotic bias of 2SLS moves towards that of OLS, the sampling distribution becomes extremely fat-tailed and distorted, conventional standard errors fail completely, and even devastating spurious causality can result!",
                prereq="Prerequisite: the Staiger-Stock weak-instrument and finite-sample-bias results",
                radar_hit="boundary"
            ),
            "trap_econ_2_2": TrapDetail(
                title="🚨 Mathematical blind spot on degrees of freedom and identification: exact identification makes a statistical exogeneity test impossible",
                desc="An over-identification test (such as the Sargan test or the Hansen J statistic) presupposes that the number of instruments m strictly exceeds the number of endogenous variables k (m > k). Under exact identification the residuals are exactly orthogonal to the fitted values and the residual sum of squares has 0 degrees of freedom, so no test can be performed at all!",
                prereq="Prerequisite: the definition of the degrees of freedom of the Sargan-Hansen over-identification statistic",
                radar_hit="precision"
            ),
            "trap_econ_2_3": TrapDetail(
                title="🚨 Exclusion restriction fully inverted: a valid instrument must never directly affect the dependent variable!",
                desc="The strict definition of the exclusion restriction is that the instrument Z may affect wages only indirectly, through the single channel of the endogenous variable Educ! If Z itself directly determines wages, then that variable enters the disturbance of the original equation and exogeneity is destroyed!",
                prereq="Prerequisite: causal DAGs (directed acyclic graphs) and the exclusion-restriction theorem",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Causal inference · topology of instrument identification and exogeneity constraints",
            nodes=[
                GraphNode(id="c1", label="2SLS instrument identification", type="core", x=260, y=140),
                GraphNode(id="p1", label="Exogenous exclusion: Cov(Z,u)=0", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Strong relevance: first-stage F > 10", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Weak-instrument trap: F < 10 causes severe bias", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Misplacement trap: Sargan test under exact identification", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Causal exogeneity constraint"),
                GraphEdge(from_node="p2", to_node="c1", label="Identification-strength gate"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (underestimating the damage of a weak instrument)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (ignoring the test's degrees-of-freedom constraint)"),
            ]
        ),
        socratic_prompt="Draw a causal arrow in your mind: if areas close to a university are themselves high-wage coastal metropolises (that is, Z directly affects Wage), how could we ever distinguish whether the higher wages come from more schooling or from being born in a big city? That is exactly why the exclusion restriction matters so much!"
    ),

    QuizItem(
        id="econ_3",
        subject="econ",
        difficulty="★★★★☆",
        tag="Violation of classic assumptions · heteroskedasticity, the White test and robust standard errors",
        stem="In a cross-sectional regression of household consumption expenditure, the dispersion of saving and consumption elasticities among wealthy households is far greater than among low-income households, so the error term exhibits heteroskedasticity that fans out as income rises (Var(u_i|X_i) = σ_i²). Which of the following statements about the harm heteroskedasticity does to OLS, the available tests and the corrective strategies fully conforms to modern empirical practice?",
        options=[
            OptionItem(key="A", text="Under heteroskedasticity the OLS estimator β̂ loses both unbiasedness and consistency entirely, and the estimated regression coefficients are worthless as a reference", is_correct=False, trap_id="trap_econ_3_1"),
            OptionItem(key="B", text="The White test requires the researcher to know the exact mathematical form of the heteroskedasticity in advance (for example an exponential or a linear form) before it can be applied", is_correct=False, trap_id="trap_econ_3_2"),
            OptionItem(key="C", text="The OLS estimator remains unbiased and consistent, but the standard errors computed by the conventional formula are severely biased; the standard modern practice is to use White heteroskedasticity-robust standard errors directly for statistical inference", is_correct=True),
            OptionItem(key="D", text="Weighted least squares (WLS) is unconditionally superior to OLS with robust standard errors in every situation and can never introduce new model-specification error", is_correct=False, trap_id="trap_econ_3_3"),
        ],
        explanation="[Authoritative examination analysis · consequences of heteroskedasticity and robust inference]: (1) Heteroskedasticity violates the homoskedasticity assumption and destroys the 'efficiency (BLUE)' part of the Gauss-Markov theorem, but it leaves the expectation E(β̂)=β completely unaffected, so the OLS estimator remains unbiased and consistent! (2) The truly fatal injury of heteroskedasticity is that Var(β̂) computed by the conventional formula is biased, which distorts t statistics and confidence intervals across the board! (3) The White test uses an auxiliary regression and requires no presupposed form of heteroskedasticity; the current gold standard in the literature is to report OLS coefficients with heteroskedasticity-robust standard errors (for example ', robust' in Stata)!",
        traps={
            "trap_econ_3_1": TrapDetail(
                title="🚨 High-frequency property-confusion pitfall: mistaking 'impaired efficiency' for a 'loss of unbiasedness'",
                desc="60% of the class will blurt out 'the OLS estimator is biased'! The sole premise for unbiasedness is exogeneity, E(u|X)=0. A larger or smaller residual variance only makes the estimator's sampling fluctuation larger; it never shifts the centre of the estimator's population average systematically!",
                prereq="Prerequisite: the breakpoint between the unbiasedness condition and the BLUE efficiency condition",
                radar_hit="recall"
            ),
            "trap_econ_3_2": TrapDetail(
                title="🚨 Confusion over test mechanics: mistaking the White test for a test that depends on a specific functional form",
                desc="The White test's greatest breakthrough is precisely that it runs an auxiliary regression of the squared residuals on the first-order terms, squares and interactions of all regressors, so the researcher never needs to guess which particular function generates the heteroskedasticity!",
                prereq="Prerequisite: the construction of the White (1980) asymptotic large-sample auxiliary regression",
                radar_hit="boundary"
            ),
            "trap_econ_3_3": TrapDetail(
                title="🚨 Blind-faith WLS anti-pattern: WLS with the wrong weights is even worse than OLS",
                desc="Feasible generalised least squares (FGLS/WLS) is asymptotically efficient only when the researcher guesses the structure of the heteroskedasticity function correctly. If the weighting matrix is misspecified, the WLS estimator actually loses consistency, which is why almost all top-tier modern empirical papers use OLS with robust standard errors!",
                prereq="Prerequisite: the robustness risk of FGLS and the sandwich variance estimator",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="Heteroskedasticity · causes, consequences and the White robust-inference map",
            nodes=[
                GraphNode(id="c1", label="Heteroskedasticity (Var(u|X)=σi²)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Coefficients stay unbiased and consistent", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Remedy: White robust standard errors", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Misconception: OLS coefficients judged biased", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Misconception: applying WLS weights blindly", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Exogeneity assumption holds"),
                GraphEdge(from_node="p2", to_node="c1", label="Sandwich covariance correction"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (conflating high variance with a biased expectation)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (ignoring weight misspecification)"),
            ]
        ),
        socratic_prompt="Think: if an electronic scale occasionally jitters and its readings scatter more (high variance), but the average of 100 weighings is still perfectly accurate (unbiased), should we throw the scale away, or give it a proper manual that correctly computes its error range (robust standard errors)?"
    ),

    # =========================================================================
    # 4. SE (Software Engineering and System Design)
    # =========================================================================
    QuizItem(
        id="se_1",
        subject="se",
        difficulty="★★★☆☆",
        tag="Software process models · the trade-off between agile Scrum and the waterfall model",
        stem="In a core business-system development project for a smart hospital, the requirements for emergency-department rostering and health-insurance microservice interfaces change extremely often and unpredictably under policy influence, whereas the underlying archival storage module for patients' core electronic medical records is bound by the exceptionally strict compliance and audit-traceability requirements of the National Health Commission's Tertiary Hospital Accreditation Standards. As to the choice of software process model for this project, which of the following strategies is the most scientifically sound?",
        options=[
            OptionItem(key="A", text="Impose a pure waterfall model and completely freeze all health-insurance and rostering requirements specifications in phase one before coding may begin", is_correct=False, trap_id="trap_se_1_1"),
            OptionItem(key="B", text="Adopt a hybrid process model: the strongly compliant and stable lower layer uses architecture-first design and rigorous documentation, while the frequently changing business services use two-week Scrum sprint iterations for validation", is_correct=True),
            OptionItem(key="C", text="Abandon all software architecture design documents and test cases entirely, adopt extreme programming (XP) wholesale, and rely on daily pair-programming refactoring to pass every national compliance review", is_correct=False, trap_id="trap_se_1_2"),
            OptionItem(key="D", text="Adopt the big-bang model, with developers working through the night in the final week before the deadline to deliver all the code in one go", is_correct=False, trap_id="trap_se_1_3"),
        ],
        explanation="[Authoritative examination analysis · trade-offs among software lifecycle models]: According to Boehm's software-engineering economics law, the cost of a requirements change grows exponentially with the project lifecycle. Imposing the waterfall model on 'highly volatile business' inevitably causes severe schedule and budget overruns, while blindly imposing extreme zero-documentation development on the 'highly compliant lower layer' inevitably causes acceptance failure. Mature industrial practice generally adopts a hybrid agile dual-track approach: an architecture-constrained baseline under control, with agile iteration for the front-end application!",
        traps={
            "trap_se_1_1": TrapDetail(
                title="🚨 Traditional dogmatic waterfall trap: forcibly 'freezing requirements' in volatile business",
                desc="Many students new to software engineering worship the rigour of the waterfall model without noticing that, when external business or policy changes month after month, the strong dependence between consecutive waterfall phases traps the whole team in an endless 'requirements-change submission process' and in large-scale code rewrites!",
                prereq="Prerequisite: Boehm's exponential cost-of-change curve and the limitations of waterfall",
                radar_hit="boundary"
            ),
            "trap_se_1_2": TrapDetail(
                title="🚨 Dogmatic misreading of the Agile Manifesto trap: equating 'embracing change' with 'no documentation and no architecture'",
                desc="The Agile Manifesto actually says 'working software over comprehensive documentation', never 'no documentation'! In safety-critical systems such as healthcare, finance and aerospace, the requirements traceability matrix (RTM) and interface-contract documents are statutory veto items!",
                prereq="Prerequisite: the core principles of the Agile Manifesto and compliant systems-engineering norms",
                radar_hit="recall"
            ),
            "trap_se_1_3": TrapDetail(
                title="🚨 Anti-engineering development trap: the big-bang model is synonymous with chaotic engineering",
                desc="The big-bang model, with no plan, no phase reviews and no test gates, violates every basic principle of software engineering and is the number-one anti-pattern that sends the vast majority of software projects to the scrap heap!",
                prereq="Prerequisite: the nature of the software crisis and modern software-engineering control theory",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="Software process models · agile iteration versus architecture compliance",
            nodes=[
                GraphNode(id="c1", label="Hybrid agile process model", type="core", x=260, y=140),
                GraphNode(id="p1", label="Lower layer, strong compliance: controlled architecture baseline", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Volatile business layer: two-week Scrum iterations", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Dogmatic waterfall: forcibly freezing volatile requirements", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Pseudo-agile: blindly discarding all architecture documents", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Compliance quality baseline"),
                GraphEdge(from_node="p2", to_node="c1", label="Rapidly embracing change"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (dogmatic, rigid development)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (letting chaos reign)"),
            ]
        ),
        socratic_prompt="Think: if a building's foundations and load-bearing beams (the compliance core) must be drawing-reviewed and absolutely immovable, while the office partitions on the top floor (the volatile business) are rearranged by tenants at will, should we demolish and rebuild everything, or keep the foundations solid and use movable lightweight partitions?"
    ),

    QuizItem(
        id="se_2",
        subject="se",
        difficulty="★★★★☆",
        tag="Object-oriented architecture design · the SOLID principles and the dependency inversion principle (DIP)",
        stem="When designing a knowledge-graph extraction engine for multi-source academic literature, the upper-layer core analysis class LiteratureAnalyzer instantiates a concrete MySQL database client by hard-coding (that is, this.db = new MySQLClient()). Business expansion now requires support for the distributed graph database Neo4j and the vector database Milvus. According to the dependency inversion principle (DIP) among the SOLID design principles, how should the refactoring best be carried out?",
        options=[
            OptionItem(key="A", text="Add a large number of if-else or switch-case statements inside LiteratureAnalyzer so that, depending on an injected environment variable, it runs the private operation code of each different database", is_correct=False, trap_id="trap_se_2_1"),
            OptionItem(key="B", text="Abstract a unified IKnowledgeStorage contract interface so that both the upper-layer LiteratureAnalyzer and the concrete MySQLClient/Neo4jClient depend only on that abstraction, decoupling them through constructor dependency injection (DI)", is_correct=True),
            OptionItem(key="C", text="Make the Neo4jClient class forcibly inherit from MySQLClient and override its relational query methods", is_correct=False, trap_id="trap_se_2_2"),
            OptionItem(key="D", text="Consolidate all database operation logic into one global public god class, GlobalDBManager, and have business classes call its static methods directly", is_correct=False, trap_id="trap_se_2_3"),
        ],
        explanation="[Authoritative examination analysis · SOLID principles and dependency inversion (DIP)]: (1) Definition of the dependency inversion principle: high-level modules should not depend on low-level modules — both should depend on abstractions; abstractions should not depend on details — details should depend on abstractions. (2) Option B introduces the IKnowledgeStorage interface, removing the tight coupling between the high-level analysis class and the underlying persistence technology; adding a graph or vector database then merely requires a new implementation class, with no change to existing business logic, and it perfectly satisfies the open-closed principle (OCP)!",
        traps={
            "trap_se_2_1": TrapDetail(
                title="🚨 Branch-proliferation code-smell trap: a serious violation of the open-closed principle (OCP)",
                desc="Extending an underlying implementation with large numbers of conditional branches (if-else) is the engineering smell beginners commit most often! Every new database integration requires editing high-level business code and recompiling and retesting, which very easily introduces regression bugs!",
                prereq="Prerequisite: the open-closed principle (OCP: open for extension, closed for modification)",
                radar_hit="trapDefense"
            ),
            "trap_se_2_2": TrapDetail(
                title="🚨 Deep pit of inheritance abuse: a serious violation of the Liskov substitution principle (LSP)",
                desc="Graph databases and relational databases simply have no 'is-a' derivation-substitution relationship in data model, transaction semantics or query contract! Forcing inheritance wantonly breaks the base-class contract, so the subclass cannot safely substitute for the parent!",
                prereq="Prerequisite: the Liskov substitution principle (LSP) and design by contract (DbC)",
                radar_hit="boundary"
            ),
            "trap_se_2_3": TrapDetail(
                title="🚨 God-class tight-coupling trap: creating a single point of failure and strangling unit tests",
                desc="Introducing a global all-purpose god class is a typical anti-pattern: it leaves the system with extremely low cohesion and extremely high coupling, muddles global state, and makes dependency mocking in unit tests completely impossible!",
                prereq="Prerequisite: the single-responsibility principle (SRP) and the isolation requirements of unit-test mocking",
                radar_hit="synthesis"
            )
        },
        graph=GraphData(
            title="SOLID architecture · dependency inversion and interface-segregation design map",
            nodes=[
                GraphNode(id="c1", label="Dependency inversion principle (DIP)", type="core", x=260, y=140),
                GraphNode(id="p1", label="Abstract contract interface (IKnowledgeStorage)", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Dependency-injection decoupling (DI/IoC)", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Code smell: if-else breaks OCP", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Code smell: reckless inheritance breaks LSP", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Program to an interface"),
                GraphEdge(from_node="p2", to_node="c1", label="Inversion-of-control implementation"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (hard-binding business logic to underlying technology)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (abusing inheritance to reuse code)"),
            ]
        ),
        socratic_prompt="Picture the power sockets at home: the national-standard three-pin socket defines an abstract specification (the interface), and whether it is a desk lamp, a computer or a refrigerator (the implementations), anything that meets the plug specification can be plugged in and works. If every time we bought a new appliance we had to break open the wall and rewire (modify the business code), could such a design last?"
    ),

    QuizItem(
        id="se_3",
        subject="se",
        difficulty="★★★★☆",
        tag="Software quality assurance · boundary value analysis and mutation testing",
        stem="While developing the GPA calculation module of a student records management system, a function requires that the credit value of a single course fall within the valid interval [0.5, 10.0]. Regarding black-box test-case design for this module and the measurement of automated test-suite adequacy, which of the following statements is entirely correct?",
        options=[
            OptionItem(key="A", text="As long as the test suite reaches 100% line coverage, that is sufficient proof that all boundary-value defects have been eliminated and no further quality checks are needed", is_correct=False, trap_id="trap_se_3_1"),
            OptionItem(key="B", text="Boundary value analysis (BVA) should select not only values on and inside the boundaries (such as 0.5, 0.6, 9.9, 10.0) but also invalid inputs immediately outside them (such as 0.4, 10.1) to verify defensive interception; mutation testing objectively measures the true killing power of the test cases by planting mutants in the source code", is_correct=True),
            OptionItem(key="C", text="Boundary value analysis requires testers to enter only valid data inside the legal range and strictly forbids any negative or out-of-range invalid data", is_correct=False, trap_id="trap_se_3_2"),
            OptionItem(key="D", text="Mutation testing is a white-box stress-testing tool specifically for measuring server CPU utilisation when 100,000 people enrol in courses concurrently", is_correct=False, trap_id="trap_se_3_3"),
        ],
        explanation="[Authoritative examination analysis · boundary value testing and the mutation kill rate]: (1) The overwhelming majority of program bugs occur at input and output boundaries, so boundary value analysis (BVA) must include both positive and negative neighbouring boundary values (such as 0.4 and 10.1 being intercepted); (2) the coverage illusion: 100% statement coverage can perfectly well contain large numbers of assertion-free weak tests! Mutation testing automatically produces code mutants by, for example, changing `>=` to `>`, or `+` to `-`; only when a test case makes a mutant fail (is 'killed') does the suite demonstrate genuine defect-detection capability!",
        traps={
            "trap_se_3_1": TrapDetail(
                title="🚨 False sense of coverage security trap: high line coverage ≠ high defect-detection power",
                desc="This is the most dangerous blind spot in software-engineering quality gates! The fact that test code executed every line does not mean it asserted the logical correctness of every line! If the test cases contain no assert at all, coverage can still read 100%, yet the mutation kill rate drops straight to 0!",
                prereq="Prerequisite: test-adequacy criteria and the definition of the mutation score",
                radar_hit="trapDefense"
            ),
            "trap_se_3_2": TrapDetail(
                title="🚨 Missing negative-testing trap: skipping out-of-boundary interception tests leads straight to production crashes",
                desc="Testing only valid data (positive testing) is a typical symptom of fragile software. Robustness testing must cover the invalid equivalence classes immediately outside the boundaries to ensure that exceptions are safely caught and raised as controlled errors, rather than escaping as unhandled exceptions that crash the system!",
                prereq="Prerequisite: equivalence partitioning and the robustness boundary-value analysis matrix",
                radar_hit="boundary"
            ),
            "trap_se_3_3": TrapDetail(
                title="🚨 Test-type mismatch trap: mistaking 'mutation testing' for 'performance load testing'",
                desc="Mutation testing is the famous 'testing the tests' advanced meta-testing technique; it belongs to the field of fault injection and test-suite capability evaluation and has nothing whatsoever to do with performance load testing!",
                prereq="Prerequisite: fault-injection mechanisms and the classification of automated mutation operators",
                radar_hit="recall"
            )
        },
        graph=GraphData(
            title="Quality assurance · topology of boundary value analysis and mutation-test killing power",
            nodes=[
                GraphNode(id="c1", label="Mutation testing", type="core", x=260, y=140),
                GraphNode(id="p1", label="BVA: sampling across positive and negative boundaries", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Breaking weak assertions: kill-rate evaluation", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Vanity trap: believing in 100% line coverage", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Concept trap: mistaking mutation testing for load testing", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Sensitivity to high-risk boundaries"),
                GraphEdge(from_node="p2", to_node="c1", label="Test-case quality measurement"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (ignoring assertion effectiveness)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (conflating test types)"),
            ]
        ),
        socratic_prompt="Think: if a security guard merely pushes open the door of every room in the company and glances inside (100% line coverage), but he has no idea who a thief is (no assert was written), then when a real thief carries the computers out of a room (a mutant is introduced), can that guard raise the alarm?"
    ),

    # =========================================================================
    # 5. OPERATIONS RESEARCH (Operations Research and Optimisation Modelling · Core, Year 2 Semester 1)
    # =========================================================================
    QuizItem(
        id="or_1",
        subject="or",
        difficulty="★★★☆☆",
        tag="Planning modelling · physical non-negativity of decision variables and constraint boundaries",
        stem="An equipment manufacturer plans to produce two industrial components, A and B; each component consumes steel, labour hours and CNC milling-machine hours. When building a linear programming (LP) model that maximises total sales profit (max Z = 300x₁ + 500x₂), which of the following statements about the elements of the mathematical model and the standard-form conventions is entirely correct?",
        options=[
            OptionItem(key="A", text="As long as the objective function is linear, the decision variables x₁ and x₂ may take any negative real values; the model need not define physical non-negativity constraints because the solver corrects them automatically", is_correct=False, trap_id="trap_or_1"),
            OptionItem(key="B", text="The non-negativity constraints x₁ ≥ 0 and x₂ ≥ 0 must be added strictly to the constraint set; if the problem is infeasible, that means the intersection of the constraint hyperplanes — the feasible region — is the empty set, not that the objective diverges to positive infinity", is_correct=True),
            OptionItem(key="C", text="The feasible region of a linear programming model is necessarily a non-convex open space, so genetic algorithms or simulated annealing must be used to search the surface for a local optimum", is_correct=False, trap_id="trap_or_2"),
            OptionItem(key="D", text="To convert a cost-minimisation model into the standard maximisation model, one need only multiply the objective coefficients by -1; the inequality directions of all remaining constraints must stay exactly as they are", is_correct=False, trap_id="trap_or_3"),
        ],
        explanation="[Authoritative examination analysis · Hamdy Taha's planning modelling and standard form]: (1) Decision variables represent real physical entities or production and sales quantities and must satisfy non-negativity constraints ($x_j \\ge 0$), otherwise absurd solutions such as producing a negative number of components appear; (2) the feasible region of a linear programme is necessarily a convex polyhedron bounded by the intersection of hyperplanes, and the extreme point theorem guarantees that an optimal solution is attained at an extreme point; infeasibility means the constraints are mutually exclusive so that the intersection forming the feasible region is empty!",
        traps={
            "trap_or_1": TrapDetail(
                title="🚨 Detached-from-physical-reality trap: omitting the non-negativity constraints",
                desc="This is the serious error operations-research beginners commit most often in modelling! A computer solver understands only pure symbolic logic: if x₁ ≥ 0 is omitted, the arithmetic may return x₁ = -100 and a spuriously high profit, which makes the plan completely unusable in engineering terms!",
                prereq="Prerequisite: the three standard-form requirements of a linear programme and the non-negativity axiom",
                radar_hit="boundary"
            ),
            "trap_or_2": TrapDetail(
                title="🚨 Misjudging the geometry of the feasible region trap: treating a convex polyhedron as a non-convex surface",
                desc="All constraints of a linear programme are linear first-order inequalities, and the feasible region formed by the intersection of hyperplane half-spaces is strictly a convex set — never a non-convex surface! The simplex method iterates along extreme-point boundaries to find the global optimum!",
                prereq="Prerequisite: the definition of a convex set and the extreme point theorem",
                radar_hit="recall"
            ),
            "trap_or_3": TrapDetail(
                title="🚨 Careless standard-form conversion trap: constraint directions not adjusted in tandem",
                desc="When converting minimisation to maximisation, besides negating the objective function, multiplying both sides of an inequality by a negative sign requires the inequality direction to be strictly reversed, or non-negative slack variables must be introduced to obtain the equality standard form!",
                prereq="Prerequisite: LP duality theory and the simplex standard-form transformation matrix",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Operations Research Chapter 1 · linear programming modelling and solution-space topology",
            nodes=[
                GraphNode(id="c1", label="Three elements of a planning model", type="core", x=260, y=140),
                GraphNode(id="p1", label="Physical non-negativity constraint x ≥ 0", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Extreme points of a convex polyhedron feasible region", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: omitting non-negative output", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: wrongly judging the feasible region non-convex", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Physical reality boundary"),
                GraphEdge(from_node="p2", to_node="c1", label="Extreme-point optimality guarantee"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (detached from real-world meaning)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (confusing the geometric topology)"),
            ]
        ),
        socratic_prompt="Think: if a bakery wants to work out how many croissants to bake tomorrow to earn the most money, and the solver reports that 'baking minus 5 croissants' is the most profitable option, could that be carried out in the physical world? Why must mathematical formulations lock down physical boundaries with constraints?"
    ),

    # =========================================================================
    # 6. MANAGEMENT INFORMATION SYSTEMS (Management Information Systems · Core, Year 2 Semester 1)
    # =========================================================================
    QuizItem(
        id="mis_1",
        subject="mis",
        difficulty="★★★☆☆",
        tag="Organisational system levels · TPS-DSS coordination and the C2M reverse supply chain",
        stem="A retail manufacturing enterprise is advancing its digital transformation. When analysing Laudon's classic information-system architecture and the new-retail C2M (Customer-to-Manufacturer) reverse-customisation business model, which of the following statements about the division of labour among business-system levels and value-chain coordination is entirely correct?",
        options=[
            OptionItem(key="A", text="The enterprise strategic decision support system (ESS) should connect in real time to every small transaction on the point-of-sale terminals and present each one to board executives for daily verification", is_correct=False, trap_id="trap_mis_1"),
            OptionItem(key="B", text="The TPS (transaction processing system) sits at the bottom layer supporting daily high-frequency structured business transactions (such as order creation and inventory deduction); the C2M model aggregates long-tail demand through social fission such as group buying and connects it directly to factory production, and its core value lies in using algorithms to predict demand precisely and eliminate intermediate agents and the inventory bullwhip effect", is_correct=True),
            OptionItem(key="C", text="A modern enterprise management information system (MIS) consists purely of IT tools such as computer software and cloud-server hardware and has nothing to do with organisational restructuring, business process reengineering (BPR) or staff training", is_correct=False, trap_id="trap_mis_2"),
            OptionItem(key="D", text="The main purpose of an ERP (enterprise resource planning) system is to erect stricter data barriers between departments and prevent financial and production data from being shared across systems", is_correct=False, trap_id="trap_mis_3"),
        ],
        explanation="[Authoritative examination analysis · Laudon's management information systems and digital new retail]: (1) The TPS records daily deterministic operations at the bottom layer, while mid- and senior-level decision systems (MIS/DSS/ESS) distil higher-order business insight through aggregation and modelling; (2) C2M reverse customisation relies on digital long-tail aggregation to eliminate multi-tier intermediaries and dampen the bullwhip effect; (3) an MIS is a sociotechnical system combining technology, people and organisation — emphatically not a pure hardware purchase!",
        traps={
            "trap_mis_1": TrapDetail(
                title="🚨 Data-granularity mismatch trap: executive dashboards conflated with bottom-layer transaction logs",
                desc="Presenting unaggregated bottom-layer transaction detail to executives is a classic information-architecture anti-pattern! Executives need macro strategic dashboards and trend indicators; raw detail causes information overload!",
                prereq="Prerequisite: the data-granularity theory of the enterprise pyramid levels (TPS/MIS/DSS/ESS)",
                radar_hit="boundary"
            ),
            "trap_mis_2": TrapDetail(
                title="🚨 Technological-determinism trap: equating IT tools with systemic change",
                desc="Buying ERP/CRM software does not amount to system success! Without business process reengineering (BPR), organisational change management and aligned staff incentives, a go-live often becomes mere decoration or even triggers organisational turmoil!",
                prereq="Prerequisite: the sociotechnical paradigm of information systems and business process reengineering (BPR)",
                radar_hit="recall"
            ),
            "trap_mis_3": TrapDetail(
                title="🚨 Reversed judgement of the enterprise integration hub: ERP removes islands rather than building barriers",
                desc="The core mission of ERP is precisely to break down departmental barriers and information silos and to establish a single source of truth (SSOT) integrating finance, purchasing-sales-inventory and manufacturing!",
                prereq="Prerequisite: the core ERP architecture and the enterprise's end-to-end business integration chain",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Management information systems · sociotechnical paradigm and enterprise integration architecture",
            nodes=[
                GraphNode(id="c1", label="Enterprise four-level system pyramid", type="core", x=260, y=140),
                GraphNode(id="p1", label="Bottom layer, high-frequency transactions: TPS", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="C2M reverse supply-chain algorithms", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: granularity mismatch — executives shown raw detail", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: mistaking tool purchase for transformation", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Foundation of structured data sources"),
                GraphEdge(from_node="p2", to_node="c1", label="Eliminating intermediaries and the bullwhip effect"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (information-overload misalignment)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (technological-determinism bias)"),
            ]
        ),
        socratic_prompt="Think: if a hospital director had to review, one by one, the system log of every outpatient who paid a 10-yuan registration fee, would he still have time to plan the hospital's medical-research strategy for the year? Why must information systems aggregate and abstract data at different levels according to management level?"
    ),

    # =========================================================================
    # 7. PROBABILITY & STATISTICS (Probability Theory and Mathematical Statistics · Core, Year 2 Semester 1)
    # =========================================================================
    QuizItem(
        id="prob_stat_1",
        subject="prob_stat",
        difficulty="★★★★☆",
        tag="Prior-posterior inversion · Bayes' theorem and testing event independence",
        stem="A university laboratory has developed a non-destructive optical detector for nanoscale micro-cracks in chips. For a batch of wafer dies, the prior probability of the micro-crack is P(A) = 0.002 (two per thousand). The detector's sensitivity, i.e. the probability of a positive reading given a cracked chip, is P(+|A) = 0.99; its false-positive rate, i.e. a positive reading given an uncracked chip, is P(+|Ā) = 0.05. A die is drawn at random and tests positive. Regarding the true posterior probability P(A|+) that the die really has a micro-crack, and the basic theory of probability, which of the following statements is entirely correct?",
        options=[
            OptionItem(key="A", text="Since the detector's positive accuracy is as high as 99%, the probability that this positively tested chip has a micro-crack must be 99%, and the prior prevalence need not be considered", is_correct=False, trap_id="trap_stat_1"),
            OptionItem(key="B", text="Two mutually exclusive events (incompatible, AB=∅) are equivalent to two independent events (P(AB)=P(A)P(B)), so mutually exclusive events never influence each other", is_correct=False, trap_id="trap_stat_2"),
            OptionItem(key="C", text="Applying Bayes' theorem in reverse, and constrained by the extremely low prior base rate (0.002), the true posterior probability is P(A|+) = (0.002×0.99) / (0.002×0.99 + 0.998×0.05) ≈ 3.81%; and if two events with positive probability are independent, they can never be mutually exclusive (they must be able to occur together)", is_correct=True),
            OptionItem(key="D", text="The sum of the probabilities of all values of a discrete random variable may exceed 1, provided each individual probability is non-negative", is_correct=False, trap_id="trap_stat_3"),
        ],
        explanation="[Authoritative examination analysis · Bayes' inversion formula and the false-positive paradox]: (1) In rare-event screening the extremely low prior probability (0.002) means that even with high sensitivity (99%), the overwhelming majority of positive results come from the small false-positive fraction of the huge healthy sample (0.998×0.05 ≈ 0.0499), and the true posterior is only about 3.81%! (2) Mutual exclusivity and independence are fundamentally opposed: if P(A)>0, P(B)>0 and the events are mutually exclusive, then P(AB)=0 ≠ P(A)P(B), so mutually exclusive events are necessarily dependent!",
        traps={
            "trap_stat_1": TrapDetail(
                title="🚨 Base rate fallacy: mistaking sensitivity for the confirmed posterior rate",
                desc="This is the probability pitfall that 72% of students — and even seasoned engineers — fall into most often! The key premise of an extremely low prior prevalence is ignored, and the conditional probability P(+|A) is conflated with P(A|+)!",
                prereq="Prerequisite: normalisation of the conditional-probability measure and the law of total probability",
                radar_hit="boundary"
            ),
            "trap_stat_2": TrapDetail(
                title="🚨 High-risk trap: conflating set-theoretic exclusivity with statistical independence",
                desc="Mutual exclusivity says 'the intersection is empty, so they cannot occur together'; independence says 'the occurrence of one does not change the probability of the other at all'! If B absolutely cannot occur when A occurs, then A imposes an extremely strong negative informational constraint on B — how could they be independent?",
                prereq="Prerequisite: the strict mathematical criterion for statistical independence, P(AB)=P(A)P(B)",
                radar_hit="recall"
            ),
            "trap_stat_3": TrapDetail(
                title="🚨 Missing normalisation property of the discrete probability mass function (PMF)",
                desc="Kolmogorov's second axiom of normalisation states explicitly that P(Ω)=1: the probabilities of a discrete random variable over the entire sample space must sum to exactly 1 and can never exceed 1!",
                prereq="Prerequisite: Kolmogorov's axiomatic system and PMF normalisation",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Probability and statistics · axiomatic measure and the Bayesian prior-posterior topology",
            nodes=[
                GraphNode(id="c1", label="Bayesian posterior-update theorem", type="core", x=260, y=140),
                GraphNode(id="p1", label="Prior base rate P(A)=0.002", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Normalisation of the total-probability denominator", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: mistaking sensitivity for the posterior rate", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: conflating exclusivity with independence", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Inferring cause from effect: the core prior"),
                GraphEdge(from_node="p2", to_node="c1", label="Partition of the denominator into a complete event group"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (base rate fallacy)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (conflating geometric and informational measures)"),
            ]
        ),
        socratic_prompt="Think: suppose only 1 person in the world has a rare disease, and a hospital has a test with 99.9% accuracy. If all 8 billion people on Earth were tested, 8 million healthy people would be falsely reported positive while only 1 is truly ill. If you received a positive report, would your chance of actually having the disease really be 99.9%?"
    ),

    # =========================================================================
    # 8. MARKETING (Marketing Principles · Core, Year 2 Semester 1)
    # =========================================================================
    QuizItem(
        id="mkt_1",
        subject="mkt",
        difficulty="★★★☆☆",
        tag="STP strategic positioning · 4Ps coordination and Porter's competitive strategy",
        stem="When analysing China's freshly made coffee market (using the '9.9-yuan price war' between Luckin Coffee and Cotti Coffee as a real-world case), which of the following analyses of the implementation of the classic STP strategic marketing framework and Porter's five-forces competitive strategy is entirely correct?",
        options=[
            OptionItem(key="A", text="The best market-positioning strategy for a mature brand is to 'try to cater to all the needs of every consumer group in society', so market segmentation and target selection are unnecessary", is_correct=False, trap_id="trap_mkt_1"),
            OptionItem(key="B", text="Luckin relies on a dense network of lower-tier-city stores and a fully digital, automated ordering process to target, in its chosen segment, white-collar customers who value cost-effectiveness and convenience; a firm that relies only on low-price subsidies in a price war without achieving supply-chain scale cost leadership or differentiation in consumers' minds easily becomes 'stuck in the middle' and severely erodes its brand equity", is_correct=True),
            OptionItem(key="C", text="The 'Promotion' element of the marketing mix (4Ps) is the entire content of modern marketing, and product development and pricing have nothing to do with marketing", is_correct=False, trap_id="trap_mkt_2"),
            OptionItem(key="D", text="For a low-involvement fast-moving consumer good such as everyday freshly ground coffee, consumers spend several weeks reading ten-thousand-word industry research reports before each rational purchase", is_correct=False, trap_id="trap_mkt_3"),
        ],
        explanation="[Authoritative examination analysis · STP strategy and Porter's three generic competitive strategies]: (1) The essence of strategy lies in trade-offs; trying to satisfy everyone blurs positioning; (2) a price war is no long-term plan — a firm must have either cost leadership backed by supply-chain economies of scale or brand differentiation in consumers' minds, otherwise it degenerates into loss-making cut-throat competition; (3) the 4Ps are the coordinated whole of product, price, place and promotion!",
        traps={
            "trap_mkt_1": TrapDetail(
                title="🚨 Target-positioning over-generalisation trap: trying to please everyone",
                desc="Without segmentation there is no positioning! A firm that tries to be an all-purpose brand is usually utterly unremarkable in the minds of every segment, and its resources are quickly eaten away by differentiated rivals!",
                prereq="Prerequisite: STP theory and the assessment of target-segment attractiveness",
                radar_hit="boundary"
            ),
            "trap_mkt_2": TrapDetail(
                title="🚨 Marketing-narrowing misconception: equating marketing with discount promotions",
                desc="Many people wrongly reduce marketing to promotional discounts and overlook that Product (core value) and Place (channel control) are the durable assets that form a commercial competitive barrier!",
                prereq="Prerequisite: the 4Ps marketing-mix coordination theory and brand-equity models",
                radar_hit="recall"
            ),
            "trap_mkt_3": TrapDetail(
                title="🚨 Consumer-involvement model mismatch: applying high-involvement decision models to fast-moving consumer goods",
                desc="Freshly ground coffee is a textbook low-involvement, high-frequency impulse product: consumer decisions depend on convenience, habit and price stimuli, never on long-cycle in-depth search!",
                prereq="Prerequisite: consumer-involvement theory (the FCB grid / involvement funnel)",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Marketing · topology of STP strategic positioning and 4Ps competitive coordination",
            nodes=[
                GraphNode(id="c1", label="Core STP strategic positioning", type="core", x=260, y=140),
                GraphNode(id="p1", label="Supply-chain cost-leadership barrier", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Low-involvement FMCG decision funnel", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: over-generalising to please everyone", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: narrow discounting damages brand equity", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Economies of scale underpin the price war"),
                GraphEdge(from_node="p2", to_node="c1", label="Instant convenience and mind-share positioning"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (lacking the courage of strategic trade-offs)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (tactical discounting erodes the brand)"),
            ]
        ),
        socratic_prompt="Think: if Starbucks and Luckin suddenly gave every cup of coffee away free tomorrow, would consumers still find the coffee good when the subsidies stopped the day after? If a brand attracts customers only by cutting prices, then the moment a rival cuts one yuan more than you, will the customers you worked so hard to accumulate still be there?"
    ),

    # =========================================================================
    # 9. ACADEMIC ENGLISH (Academic English and Business Communication · Core, Year 2 Semester 1)
    # =========================================================================
    QuizItem(
        id="eng_1",
        subject="eng",
        difficulty="★★★☆☆",
        tag="Academic paper conventions · IMRaD discourse and the rhetoric of objective hedging",
        stem="When writing a high-level academic paper for international peer review, or a software-engineering final-year technical report, which of the following statements about academic register, hedging and anti-plagiarism norms is entirely correct?",
        options=[
            OptionItem(key="A", text="To make academic conclusions appear more persuasive, researchers should use absolutist assertions such as 'always, absolutely, perfectly proves' as much as possible in their papers and must never use softeners such as 'may, might, suggest'", is_correct=False, trap_id="trap_eng_1"),
            OptionItem(key="B", text="The internationally recognised IMRaD structure of academic papers (Introduction, Methods, Results, Discussion) demands rigour and objectivity; hedging devices embody academic rigour and precisely control the scope of certainty in an argument; compliant paraphrasing must thoroughly restructure the original's sentence logic, and a patchwork that merely swaps synonyms mechanically will still be judged by plagiarism-detection systems as the academic misconduct of patchwriting", is_correct=True),
            OptionItem(key="C", text="When writing the Results section of a paper, one should directly mix in large amounts of subjective speculation and personal emotional declarations that have not been tested against the experimental data", is_correct=False, trap_id="trap_eng_2"),
            OptionItem(key="D", text="Academic English permits the free and extensive use of colloquial everyday slang such as 'kids, a lot of, cool stuff' in formal papers, with no need to distinguish the spoken register from the academic written register", is_correct=False, trap_id="trap_eng_3"),
        ],
        explanation="[Authoritative examination analysis · IMRaD discourse conventions and academic integrity]: (1) Scientific conclusions must leave room for doubt; hedging devices (may, indicate, suggest, potentially) display the researcher's humility and rigour in the face of the unknown; (2) paraphrasing must restate the source in one's own syntax and logic — simple synonym substitution still counts as patchwriting plagiarism! (3) The Results section lists data objectively; only the Discussion section may develop in-depth mechanistic argument!",
        traps={
            "trap_eng_1": TrapDetail(
                title="🚨 Absolutist over-commitment trap: missing academic hedging",
                desc="Using 'absolutely' or 'perfectly proves' in academic writing is a beginner's fatal flaw! Every experiment has sampling and boundary limitations, and dogmatic assertions are easily and severely rejected in peer review!",
                prereq="Prerequisite: the objectivity of academic register and the norms of hedging rhetoric (epistemic modality)",
                radar_hit="boundary"
            ),
            "trap_eng_2": TrapDetail(
                title="🚨 Discourse-structure function misplacement trap: smuggling subjective conjecture into the Results",
                desc="Results must be purely objective, neutral facts and figures! Subjective extrapolation and hypothetical mechanistic explanations belong in the Discussion section!",
                prereq="Prerequisite: the four macro-functional divisions of IMRaD academic discourse",
                radar_hit="recall"
            ),
            "trap_eng_3": TrapDetail(
                title="🚨 Pseudo-paraphrase patchwork plagiarism trap: patchwriting is still academic misconduct",
                desc="Merely swapping 'important' for 'significant' or 'big' for 'massive' inside someone else's sentence while leaving the original author's syntactic skeleton untouched will be flagged in red by plagiarism-detection systems such as Turnitin!",
                prereq="Prerequisite: academic citation norms and the techniques of deep paraphrasing and structural restructuring",
                radar_hit="trapDefense"
            )
        },
        graph=GraphData(
            title="Academic English · the IMRaD paradigm and objective hedging discourse topology",
            nodes=[
                GraphNode(id="c1", label="IMRaD academic discourse paradigm", type="core", x=260, y=140),
                GraphNode(id="p1", label="Objective, cautious hedging", type="prereq", x=120, y=60),
                GraphNode(id="p2", label="Anti-plagiarism deep paraphrasing", type="prereq", x=400, y=60),
                GraphNode(id="t1", label="Trap: absolutist over-commitment", type="trap", x=130, y=240),
                GraphNode(id="t2", label="Trap: mechanical synonym-patchwork plagiarism", type="trap", x=390, y=240),
            ],
            edges=[
                GraphEdge(from_node="p1", to_node="c1", label="Scientific rigour in the Discussion"),
                GraphEdge(from_node="p2", to_node="c1", label="Legitimacy of the literature review"),
                GraphEdge(from_node="c1", to_node="t1", label="Common error (dogmatic absolutism)"),
                GraphEdge(from_node="c1", to_node="t2", label="Common error (flagged red by plagiarism detection)"),
            ]
        ),
        socratic_prompt="Think: if a meteorologist wrote in a paper 'it will 100% certainly rain tomorrow and there will absolutely not be a ray of sunshine', and the next day the sun came out; versus writing 'radar data show a pronounced convergence of cold and warm air masses, indicating a very high probability of rain tomorrow' — which formulation expresses the genuinely scientific attitude?"
    ),
]

def get_seed_questions() -> List[QuizItem]:
    """Return all seed quiz items."""
    return list(SEED_QUESTIONS)
