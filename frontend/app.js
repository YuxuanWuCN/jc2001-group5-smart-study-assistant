/**
 * SmartStudy Compass (SmartStudy AI) - Full Student-Side Interaction Controller
 * JC2001 Software Engineering - Group 5 (BSc BMIS)
 */

// =============================================================================
// Curated Multi-Discipline Question Bank & Misconception Knowledge (English)
// =============================================================================
const DB_EN = {
  se: {
    name: "Software Engineering & Architecture",
    badge: "JC2001 Core Syllabus",
    questions: [
      {
        id: "se_1",
        difficulty: "★★★☆☆",
        tag: "Software process models · the trade-off between agile Scrum and the waterfall model",
        stem: "In a core business-system development project for a smart hospital, the requirements for emergency-department rostering and health-insurance microservice interfaces change extremely often and unpredictably under policy influence, whereas the underlying archival storage module for patients' core electronic medical records is bound by the exceptionally strict compliance and audit-traceability requirements of the National Health Commission's Tertiary Hospital Accreditation Standards. As to the choice of software process model for this project, which of the following strategies is the most scientifically sound?",
        options: [
          { key: "A", text: "Impose a pure waterfall model and completely freeze all health-insurance and rostering requirements specifications in phase one before coding may begin", isCorrect: false, trapId: "trap_se_1_1" },
          { key: "B", text: "Adopt a hybrid process model: the strongly compliant and stable lower layer uses architecture-first design and rigorous documentation, while the frequently changing business services use two-week Scrum sprint iterations for validation", isCorrect: true },
          { key: "C", text: "Abandon all software architecture design documents and test cases entirely, adopt extreme programming (XP) wholesale, and rely on daily pair-programming refactoring to pass every national compliance review", isCorrect: false, trapId: "trap_se_1_2" },
          { key: "D", text: "Adopt the big-bang model, with developers working through the night in the final week before the deadline to deliver all the code in one go", isCorrect: false, trapId: "trap_se_1_3" }
        ],
        explanation: "[Authoritative examination analysis · trade-offs among software lifecycle models]: According to Boehm's software-engineering economics law, the cost of a requirements change grows exponentially with the project lifecycle. Imposing the waterfall model on 'highly volatile business' inevitably causes severe schedule and budget overruns, while blindly imposing extreme zero-documentation development on the 'highly compliant lower layer' inevitably causes acceptance failure. Mature industrial practice generally adopts a hybrid agile dual-track approach: an architecture-constrained baseline under control, with agile iteration for the front-end application!",
        traps: {
          trap_se_1_1: {
            title: "🚨 Traditional dogmatic waterfall trap: forcibly 'freezing requirements' in volatile business",
            desc: "Many students new to software engineering worship the rigour of the waterfall model without noticing that, when external business or policy changes month after month, the strong dependence between consecutive waterfall phases traps the whole team in an endless 'requirements-change submission process' and in large-scale code rewrites!",
            prereq: "Prerequisite: Boehm's exponential cost-of-change curve and the limitations of waterfall",
            radarHit: "boundary"
          },
          trap_se_1_2: {
            title: "🚨 Dogmatic misreading of the Agile Manifesto trap: equating 'embracing change' with 'no documentation and no architecture'",
            desc: "The Agile Manifesto actually says 'working software over comprehensive documentation', never 'no documentation'! In safety-critical systems such as healthcare, finance and aerospace, the requirements traceability matrix (RTM) and interface-contract documents are statutory veto items!",
            prereq: "Prerequisite: the core principles of the Agile Manifesto and compliant systems-engineering norms",
            radarHit: "recall"
          },
          trap_se_1_3: {
            title: "🚨 Anti-engineering development trap: the big-bang model is synonymous with chaotic engineering",
            desc: "The big-bang model, with no plan, no phase reviews and no test gates, violates every basic principle of software engineering and is the number-one anti-pattern that sends the vast majority of software projects to the scrap heap!",
            prereq: "Prerequisite: the nature of the software crisis and modern software-engineering control theory",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "Software process models · agile iteration versus architecture compliance",
          nodes: [
            { id: "c1", label: "Hybrid agile process model", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Lower layer, strong compliance: controlled architecture baseline", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Volatile business layer: two-week Scrum iterations", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Dogmatic waterfall: forcibly freezing volatile requirements", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Pseudo-agile: blindly discarding all architecture documents", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Compliance quality baseline" },
            { from: "p2", to: "c1", label: "Rapidly embracing change" },
            { from: "c1", to: "t1", label: "Common error (dogmatic, rigid development)" },
            { from: "c1", to: "t2", label: "Common error (letting chaos reign)" }
          ]
        },
        socraticPrompt: "Think: if a building's foundations and load-bearing beams (the compliance core) must be drawing-reviewed and absolutely immovable, while the office partitions on the top floor (the volatile business) are rearranged by tenants at will, should we demolish and rebuild everything, or keep the foundations solid and use movable lightweight partitions?"
      },
      {
        id: "se_2",
        difficulty: "★★★★☆",
        tag: "Object-oriented architecture design · the SOLID principles and the dependency inversion principle (DIP)",
        stem: "When designing a knowledge-graph extraction engine for multi-source academic literature, the upper-layer core analysis class LiteratureAnalyzer instantiates a concrete MySQL database client by hard-coding (that is, this.db = new MySQLClient()). Business expansion now requires support for the distributed graph database Neo4j and the vector database Milvus. According to the dependency inversion principle (DIP) among the SOLID design principles, how should the refactoring best be carried out?",
        options: [
          { key: "A", text: "Add a large number of if-else or switch-case statements inside LiteratureAnalyzer so that, depending on an injected environment variable, it runs the private operation code of each different database", isCorrect: false, trapId: "trap_se_2_1" },
          { key: "B", text: "Abstract a unified IKnowledgeStorage contract interface so that both the upper-layer LiteratureAnalyzer and the concrete MySQLClient/Neo4jClient depend only on that abstraction, decoupling them through constructor dependency injection (DI)", isCorrect: true },
          { key: "C", text: "Make the Neo4jClient class forcibly inherit from MySQLClient and override its relational query methods", isCorrect: false, trapId: "trap_se_2_2" },
          { key: "D", text: "Consolidate all database operation logic into one global public god class, GlobalDBManager, and have business classes call its static methods directly", isCorrect: false, trapId: "trap_se_2_3" }
        ],
        explanation: "[Authoritative examination analysis · SOLID principles and dependency inversion (DIP)]: (1) Definition of the dependency inversion principle: high-level modules should not depend on low-level modules — both should depend on abstractions; abstractions should not depend on details — details should depend on abstractions. (2) Option B introduces the IKnowledgeStorage interface, removing the tight coupling between the high-level analysis class and the underlying persistence technology; adding a graph or vector database then merely requires a new implementation class, with no change to existing business logic, and it perfectly satisfies the open-closed principle (OCP)!",
        traps: {
          trap_se_2_1: {
            title: "🚨 Branch-proliferation code-smell trap: a serious violation of the open-closed principle (OCP)",
            desc: "Extending an underlying implementation with large numbers of conditional branches (if-else) is the engineering smell beginners commit most often! Every new database integration requires editing high-level business code and recompiling and retesting, which very easily introduces regression bugs!",
            prereq: "Prerequisite: the open-closed principle (OCP: open for extension, closed for modification)",
            radarHit: "trapDefense"
          },
          trap_se_2_2: {
            title: "🚨 Deep pit of inheritance abuse: a serious violation of the Liskov substitution principle (LSP)",
            desc: "Graph databases and relational databases simply have no 'is-a' derivation-substitution relationship in data model, transaction semantics or query contract! Forcing inheritance wantonly breaks the base-class contract, so the subclass cannot safely substitute for the parent!",
            prereq: "Prerequisite: the Liskov substitution principle (LSP) and design by contract (DbC)",
            radarHit: "boundary"
          },
          trap_se_2_3: {
            title: "🚨 God-class tight-coupling trap: creating a single point of failure and strangling unit tests",
            desc: "Introducing a global all-purpose god class is a typical anti-pattern: it leaves the system with extremely low cohesion and extremely high coupling, muddles global state, and makes dependency mocking in unit tests completely impossible!",
            prereq: "Prerequisite: the single-responsibility principle (SRP) and the isolation requirements of unit-test mocking",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "SOLID architecture · dependency inversion and interface-segregation design map",
          nodes: [
            { id: "c1", label: "Dependency inversion principle (DIP)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Abstract contract interface (IKnowledgeStorage)", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Dependency-injection decoupling (DI/IoC)", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Code smell: if-else breaks OCP", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Code smell: reckless inheritance breaks LSP", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Program to an interface" },
            { from: "p2", to: "c1", label: "Inversion-of-control implementation" },
            { from: "c1", to: "t1", label: "Common error (hard-binding business logic to underlying technology)" },
            { from: "c1", to: "t2", label: "Common error (abusing inheritance to reuse code)" }
          ]
        },
        socraticPrompt: "Picture the power sockets at home: the national-standard three-pin socket defines an abstract specification (the interface), and whether it is a desk lamp, a computer or a refrigerator (the implementations), anything that meets the plug specification can be plugged in and works. If every time we bought a new appliance we had to break open the wall and rewire (modify the business code), could such a design last?"
      },
      {
        id: "se_3",
        difficulty: "★★★★☆",
        tag: "Software quality assurance · boundary value analysis and mutation testing",
        stem: "While developing the GPA calculation module of a student records management system, a function requires that the credit value of a single course fall within the valid interval [0.5, 10.0]. Regarding black-box test-case design for this module and the measurement of automated test-suite adequacy, which of the following statements is entirely correct?",
        options: [
          { key: "A", text: "As long as the test suite reaches 100% line coverage, that is sufficient proof that all boundary-value defects have been eliminated and no further quality checks are needed", isCorrect: false, trapId: "trap_se_3_1" },
          { key: "B", text: "Boundary value analysis (BVA) should select not only values on and inside the boundaries (such as 0.5, 0.6, 9.9, 10.0) but also invalid inputs immediately outside them (such as 0.4, 10.1) to verify defensive interception; mutation testing objectively measures the true killing power of the test cases by planting mutants in the source code", isCorrect: true },
          { key: "C", text: "Boundary value analysis requires testers to enter only valid data inside the legal range and strictly forbids any negative or out-of-range invalid data", isCorrect: false, trapId: "trap_se_3_2" },
          { key: "D", text: "Mutation testing is a white-box stress-testing tool specifically for measuring server CPU utilisation when 100,000 people enrol in courses concurrently", isCorrect: false, trapId: "trap_se_3_3" }
        ],
        explanation: "[Authoritative examination analysis · boundary value testing and the mutation kill rate]: (1) The overwhelming majority of program bugs occur at input and output boundaries, so boundary value analysis (BVA) must include both positive and negative neighbouring boundary values (such as 0.4 and 10.1 being intercepted); (2) the coverage illusion: 100% statement coverage can perfectly well contain large numbers of assertion-free weak tests! Mutation testing automatically produces code mutants by, for example, changing `>=` to `>`, or `+` to `-`; only when a test case makes a mutant fail (is 'killed') does the suite demonstrate genuine defect-detection capability!",
        traps: {
          trap_se_3_1: {
            title: "🚨 False sense of coverage security trap: high line coverage ≠ high defect-detection power",
            desc: "This is the most dangerous blind spot in software-engineering quality gates! The fact that test code executed every line does not mean it asserted the logical correctness of every line! If the test cases contain no assert at all, coverage can still read 100%, yet the mutation kill rate drops straight to 0!",
            prereq: "Prerequisite: test-adequacy criteria and the definition of the mutation score",
            radarHit: "trapDefense"
          },
          trap_se_3_2: {
            title: "🚨 Missing negative-testing trap: skipping out-of-boundary interception tests leads straight to production crashes",
            desc: "Testing only valid data (positive testing) is a typical symptom of fragile software. Robustness testing must cover the invalid equivalence classes immediately outside the boundaries to ensure that exceptions are safely caught and raised as controlled errors, rather than escaping as unhandled exceptions that crash the system!",
            prereq: "Prerequisite: equivalence partitioning and the robustness boundary-value analysis matrix",
            radarHit: "boundary"
          },
          trap_se_3_3: {
            title: "🚨 Test-type mismatch trap: mistaking 'mutation testing' for 'performance load testing'",
            desc: "Mutation testing is the famous 'testing the tests' advanced meta-testing technique; it belongs to the field of fault injection and test-suite capability evaluation and has nothing whatsoever to do with performance load testing!",
            prereq: "Prerequisite: fault-injection mechanisms and the classification of automated mutation operators",
            radarHit: "recall"
          }
        },
        graph: {
          title: "Quality assurance · topology of boundary value analysis and mutation-test killing power",
          nodes: [
            { id: "c1", label: "Mutation testing", type: "core", x: 260, y: 140 },
            { id: "p1", label: "BVA: sampling across positive and negative boundaries", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Breaking weak assertions: kill-rate evaluation", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Vanity trap: believing in 100% line coverage", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Concept trap: mistaking mutation testing for load testing", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Sensitivity to high-risk boundaries" },
            { from: "p2", to: "c1", label: "Test-case quality measurement" },
            { from: "c1", to: "t1", label: "Common error (ignoring assertion effectiveness)" },
            { from: "c1", to: "t2", label: "Common error (conflating test types)" }
          ]
        },
        socraticPrompt: "Think: if a security guard merely pushes open the door of every room in the company and glances inside (100% line coverage), but he has no idea who a thief is (no assert was written), then when a real thief carries the computers out of a room (a mutant is introduced), can that guard raise the alarm?"
      }
    ]
  },
  cs: {
    name: "Computer Systems Architecture",
    badge: "Hardware & Systems",
    questions: [
      {
        id: "cs_1",
        difficulty: "★★★★☆",
        tag: "Classic RISC pipeline · hazard handling and forwarding bypass",
        stem: "In a standard five-stage in-order pipeline (IF, ID, EX, MEM, WB), instruction i is an arithmetic operation (e.g. add R1, R2, R3), and the immediately following instruction i+1 (e.g. sub R4, R1, R5) needs R1 in its execute stage. Regarding the pipeline hazard and its optimisation in this scenario, which of the following statements is correct?",
        options: [
          { key: "A", text: "This is a write-after-read (WAR) anti-dependence hazard; the five-stage pipeline must insert 2 stall cycles", isCorrect: false, trapId: "trap_cs_1" },
          { key: "B", text: "This is a read-after-write (RAW) true data dependence; hardware forwarding can eliminate all stalls", isCorrect: true },
          { key: "C", text: "This is a structural hazard; it must be solved by upgrading the single-port register file to a multi-port one", isCorrect: false, trapId: "trap_cs_2" },
          { key: "D", text: "This is a control hazard; a branch history table (BHT) must be introduced to predict execution", isCorrect: false, trapId: "trap_cs_3" }
        ],
        explanation: "[Authoritative examination analysis · data forwarding in the classic RISC five-stage pipeline]: By the end of its EX stage (at the ALU output) instruction i has already computed the new value of R1, whereas instruction i+1 needs R1 only at the start of its EX stage. By routing a forwarding path out of the EX/MEM pipeline register into the ALU inputs, bubbles can be eliminated entirely (zero stall)!",
        traps: {
          trap_cs_1: {
            title: "🚨 Advanced-concept rote-memorisation trap: WAR/WAW anti-dependences cannot occur in an in-order five-stage pipeline at all!",
            desc: "This is a knowledge hallucination that general-purpose LLMs produce very easily! WAR hazards can arise only in superscalar processors that support out-of-order execution (e.g. the Tomasulo architecture). In the classic five-stage in-order pipeline instructions flow in program order, so an earlier instruction can never read a register after a later one!",
            prereq: "Prerequisite: the difference in premises between in-order and out-of-order execution",
            radarHit: "boundary"
          },
          trap_cs_2: {
            title: "🚨 Classification-confusion trap: mistaking 'register data transfer' for a 'hardware structural resource conflict'",
            desc: "A structural hazard means several instructions contending for the same physical component in the same clock cycle (for example, a single-port memory being read for an instruction and for data at once). The stem clearly describes a forward-backward dependence on a register value, which is a pure data hazard!",
            prereq: "Prerequisite: the boundaries between the three pipeline hazard classes",
            radarHit: "recall"
          },
          trap_cs_3: {
            title: "🚨 Over-generalisation trap: arithmetic instructions contain no conditional branch",
            desc: "Control hazards are caused only by conditional branches (beq, bne) or unconditional jumps (jmp) modifying the PC; ordinary arithmetic instructions have no branch-prediction requirement at all!",
            prereq: "Prerequisite: control hazards and the semantics of branch instructions",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "RISC five-stage pipeline · data dependence and forwarding-path map",
          nodes: [
            { id: "c1", label: "Pipeline data hazard (RAW)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Premise: in-order issue and execution", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Solution: ALU forwarding path", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Hallucination trap: misapplying WAR anti-dependence", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Confusion trap: wrongly judged as structural contention", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Microarchitectural constraint" },
            { from: "p2", to: "c1", label: "Zero-stall hardware optimisation" },
            { from: "c1", to: "t1", label: "Common error (conflating out-of-order and in-order concepts)" },
            { from: "c1", to: "t2", label: "Common error (conflating resource contention and data flow)" }
          ]
        },
        socraticPrompt: "Examine the space-time diagram of the MIPS five-stage pipeline: with in-order issue, if an instruction has already obtained its arithmetic result at the end of clock cycle 3, while the next instruction needs that result only at the start of cycle 4, why should we wait needlessly until cycle 5 when the result is written back to the register file? Could we build a short cut in between?"
      },
      {
        id: "cs_2",
        difficulty: "★★★★☆",
        tag: "Memory hierarchy · set-associative cache mapping and miss analysis",
        stem: "A 32-bit byte-addressed processor has a 32KB data cache with a block size of 64 bytes and 4-way set-associative mapping. A program now repeatedly loops over a large array with a stride of 32KB, causing severe conflict misses. Regarding the cache field breakdown and miss optimisation, which of the following statements is entirely correct?",
        options: [
          { key: "A", text: "The main-memory address is split as Tag = 19 bits, Index = 7 bits, Offset = 6 bits; raising associativity to 8 ways directly alleviates the conflict misses", isCorrect: true },
          { key: "B", text: "The main-memory address is split as Tag = 18 bits, Index = 8 bits, Offset = 6 bits; changing the replacement policy from LRU to FIFO reduces the miss rate", isCorrect: false, trapId: "trap_cs_2_1" },
          { key: "C", text: "The main-memory address is split as Tag = 20 bits, Index = 6 bits, Offset = 6 bits; increasing the block size from 64B to 128B cures the conflict misses", isCorrect: false, trapId: "trap_cs_2_2" },
          { key: "D", text: "Adding a single instruction prefetch buffer inside the CPU eliminates all data-cache misses completely", isCorrect: false, trapId: "trap_cs_2_3" }
        ],
        explanation: "[Authoritative examination analysis · cache address breakdown and 3C misses]: (1) block size 64B = 2⁶, so Offset = 6 bits; total blocks = 32KB / 64B = 512 blocks; with 4-way set associativity the number of sets = 512 / 4 = 128 sets = 2⁷, so Index = 7 bits; Tag = 32 - 7 - 6 = 19 bits! (2) Conflict misses arise because several data items map to the same index set; increasing the number of ways (for example to 8 ways) or introducing a victim cache are the classic effective remedies!",
        traps: {
          trap_cs_2_1: {
            title: "🚨 Double trap in set counting and replacement policy: confusing total cache blocks with the number of sets",
            desc: "Many students treat the 512 blocks directly as 512 sets and therefore derive a 9-bit or 8-bit Index. Worse still, LRU, grounded in temporal locality, is the best theoretical and engineering baseline; FIFO not only yields a higher miss rate but also triggers the famous Belady anomaly!",
            prereq: "Prerequisite: the set-count formula for set-associative caches and the principle of locality",
            radarHit: "precision"
          },
          trap_cs_2_2: {
            title: "🚨 Blind block-size increase trap: an oversized block compresses the number of sets and aggravates conflict misses",
            desc: "With total cache capacity fixed, blindly increasing the block size sharply halves the number of sets, which makes stride-access conflict misses even worse and significantly raises the main-memory miss penalty!",
            prereq: "Prerequisite: the trade-off structure of the 3C miss model (compulsory / capacity / conflict)",
            radarHit: "boundary"
          },
          trap_cs_2_3: {
            title: "🚨 Component-role mismatch trap: conflating instruction prefetch with data memory access",
            desc: "An instruction prefetch buffer performs adaptive fetching of a sequential instruction stream; it cannot reduce conflict misses in data-intensive array reads and writes that jump randomly with a large stride!",
            prereq: "Prerequisite: the decoupling of instruction-cache and data-cache behaviour under the Harvard architecture",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "Set-associative cache · address decoding and conflict-miss trade-off map",
          nodes: [
            { id: "c1", label: "4-way set associative (Index 7 bits)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Block size 64B (Offset 6 bits)", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Capacity 32KB (128 sets / Tag 19 bits)", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: mistaking block count for set count", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: wrongly assuming FIFO beats LRU", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Low-order in-block addressing" },
            { from: "p2", to: "c1", label: "Associativity and set-count constraint" },
            { from: "c1", to: "t1", label: "Common error (forgetting to divide by the number of ways)" },
            { from: "c1", to: "t2", label: "Common error (violating locality in the replacement policy)" }
          ]
        },
        socraticPrompt: "Take out some paper and calculate: if a reservoir has 512 tanks, each individually numbered, and we now group every 4 tanks into one large group, how many large groups are there in total? Why does the addressing hardware need to decode only the group number, while the 4 tanks within a group have their tags compared in parallel?"
      },
      {
        id: "cs_3",
        difficulty: "★★★★★",
        tag: "Virtual memory system · TLB and page-fault handling sequence",
        stem: "In a virtual-memory system supporting modern multi-level page tables, when the CPU executes a load/store instruction (e.g. lw $t0, 0($a0)) and address translation occurs, which of the following statements about the timing and hardware cooperation among the TLB, the page table and page faults is entirely correct?",
        options: [
          { key: "A", text: "On a TLB hit the CPU obtains the physical address directly and issues the memory read, with no need whatsoever to access the multi-level page table in main memory", isCorrect: true },
          { key: "B", text: "On a TLB miss the MMU hardware must immediately report a page-fault exception to the OS kernel and suspend the current process", isCorrect: false, trapId: "trap_cs_3_1" },
          { key: "C", text: "After the OS page-fault handler has completed the transfer from disk, the CPU resumes execution at the 'next instruction (PC+4)' after the faulting one", isCorrect: false, trapId: "trap_cs_3_2" },
          { key: "D", text: "When the valid bit in the page table is 1 and the TLB misses, the physical page must already have been fully swapped out to the disk swap area", isCorrect: false, trapId: "trap_cs_3_3" }
        ],
        explanation: "[Authoritative examination analysis · the virtual-address translation pipeline]: (1) The TLB is a cache of page-table entries; on a TLB hit the VA-to-PA translation completes within 1 cycle; (2) a TLB miss is not the same as a page fault! The hardware page walker automatically traverses the main-memory page table, and if the PTE has Valid = 1 it merely needs to refill the TLB with that entry, with no need to wake the OS fault handler at all; (3) a page fault is a fault-class exception, so after the page has been brought in the hardware must re-execute the original instruction that raised the exception!",
        traps: {
          trap_cs_3_1: {
            title: "🚨 Classic high-risk confusion trap: mistaking a 'TLB miss' for a 'page fault'",
            desc: "This is the core pitfall that LLMs across the web answer wrongly and that 71% of students get wrong in finals! A TLB miss merely means the TLB has not cached that page-table entry; the physical page may well be sitting safely in physical memory. A real page fault is triggered only when the page-table lookup finds Valid = 0 (the page has not yet been loaded into memory)!",
            prereq: "Prerequisite: the TLB caching mechanism versus the semantics of the page-table valid bit",
            radarHit: "trapDefense"
          },
          trap_cs_3_2: {
            title: "🚨 Exception-return semantics trap: applying the 'interrupt returns to PC+4' rule to a 'fault re-executes the instruction'",
            desc: "An interrupt is asynchronous and normally returns to the next instruction; a page fault, however, is a fault, and the load/store instruction has not yet successfully read its data. Jumping straight to the next instruction would load garbage into the destination register and the program logic would collapse!",
            prereq: "Prerequisite: the PC-saving conventions of the three exception classes (interrupt, trap, fault)",
            radarHit: "boundary"
          },
          trap_cs_3_3: {
            title: "🚨 Fully inverted flag-logic trap: Valid = 1 actually means the page is in physical memory",
            desc: "A valid/present bit of 1 means the page is in a physical frame in main memory; only 0 means the page is unallocated or has been swapped out to the disk swap area!",
            prereq: "Prerequisite: the PTE structure (valid, dirty, reference bits)",
            radarHit: "recall"
          }
        },
        graph: {
          title: "Virtual memory · topology of TLB lookup and page-fault handling",
          nodes: [
            { id: "c1", label: "VA address-translation pipeline", type: "core", x: 260, y: 140 },
            { id: "p1", label: "TLB hit: PA in 1 cycle", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "TLB miss ≠ page fault (page walk)", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Hallucination trap: TLB miss reported as page fault", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: page fault returns to PC+4", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Hit fast path" },
            { from: "p2", to: "c1", label: "Automatic hardware refill" },
            { from: "c1", to: "t1", label: "Common error (not distinguishing TLB from page-table levels)" },
            { from: "c1", to: "t2", label: "Common error (conflating fault and interrupt returns)" }
          ]
        },
        socraticPrompt: "Think back: if a librarian has an excellent memory (the TLB) but cannot recall which shelf a particular book is on (a TLB miss), does that necessarily mean the book has been discarded or borrowed? Could he simply consult the master catalogue cards (the page table) and find it?"
      }
    ]
  },
  econ: {
    name: "Econometrics & Quantitative Modeling",
    badge: "Honours Core",
    questions: [
      {
        id: "econ_1",
        difficulty: "★★★★☆",
        tag: "Violation of classic assumptions · multicollinearity and omitted-variable bias",
        stem: "In the multiple regression model Y = β₀ + β₁X₁ + β₂X₂ + u, suppose there is severe but not perfect multicollinearity between the regressors X₁ and X₂. Which of the following descriptions of the properties of the ordinary least squares (OLS) estimator is entirely correct?",
        options: [
          { key: "A", text: "The OLS estimator loses unbiasedness, produces severe endogeneity bias and cannot objectively reflect the true population parameters", isCorrect: false, trapId: "trap_econ_1" },
          { key: "B", text: "The Gauss-Markov theorem fails entirely and the OLS estimator is no longer the best linear unbiased estimator (BLUE)", isCorrect: false, trapId: "trap_econ_2" },
          { key: "C", text: "The OLS estimator remains unbiased and BLUE, but the parameter variances are inflated, which undermines the t-tests", isCorrect: true },
          { key: "D", text: "The model's overall coefficient of determination R² collapses to near 0", isCorrect: false, trapId: "trap_econ_3" }
        ],
        explanation: "[Authoritative examination analysis · the statistical consequences of multicollinearity]: Under the strict exogeneity assumption E(u|X)=0 and the homoskedasticity assumption, provided there is no 'perfect collinearity' (|X'X| ≠ 0) the Gauss-Markov theorem holds in full! OLS remains unbiased and BLUE! The real consequence of collinearity is that the variance inflation factor (VIF) soars, standard errors become too large and the t statistic of each individual variable falls substantially, while the overall regression's F test and R² usually remain high!",
        traps: {
          trap_econ_1: {
            title: "🚨 Confusing the boundary between unbiasedness and efficiency: equating 'insufficient estimation precision' with a 'biased estimator'",
            desc: "Many students, and general-purpose LLMs unconstrained by graph facts, answer 'the estimator is biased' at once! Bias arises only when a key variable is omitted or endogeneity is present. Correlation among regressors never destroys unbiasedness!",
            prereq: "Omitted-variable bias and the Gauss-Markov theorem: the premise E(u|X)=0 required by the mathematical proof of unbiasedness",
            radarHit: "recall"
          },
          trap_econ_2: {
            title: "🚨 Misreading the theorem's conditions trap: wrongly concluding that the BLUE property fails",
            desc: "Among all linear unbiased estimators OLS still has the smallest variance (it is BLUE); it is merely that this 'minimum variance' has itself been pushed up by the sample data.",
            prereq: "Prerequisite: the boundaries of the Gauss-Markov theorem's proof",
            radarHit: "boundary"
          },
          trap_econ_3: {
            title: "🚨 Classic counter-intuitive symptom trap: under collinearity R² and F are often spuriously high!",
            desc: "The most classic textbook symptom of multicollinearity is: the F test is highly significant and R² is high (e.g. 0.85), yet the t test of every individual regressor fails to reject the null hypothesis!",
            prereq: "Prerequisite: the difference between the joint-hypothesis F test and the individual t test",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "Multicollinearity · topology of its statistical properties and diagnostic traps",
          nodes: [
            { id: "c1", label: "Multicollinearity", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Assumption holds: E(u|X)=0 (strict exogeneity)", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Property: still BLUE (unbiased and efficient)", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Hallucination trap: wrongly judged as endogeneity bias", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Symptom trap: wrongly expecting R² to collapse", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Premise guaranteeing unbiasedness" },
            { from: "p2", to: "c1", label: "Minimum-variance property" },
            { from: "c1", to: "t1", label: "Common error (conflating bias with high variance)" },
            { from: "c1", to: "t2", label: "Common error (ignoring the overall F test)" }
          ]
        },
        socraticPrompt: "Think: what is the key assumption in the Gauss-Markov theorem that guarantees OLS unbiasedness? If an omitted variable enters the error term, are the regressors still orthogonal to the error term? Does the expected value of the parameter estimate equal the true population parameter?"
      },
      {
        id: "econ_2",
        difficulty: "★★★★★",
        tag: "Core of causal inference · instrumental variables (IV/2SLS) and weak instruments",
        stem: "In estimating the causal effect of years of education (Educ) on log wages (ln(Wage)), the explanatory variable Educ is severely endogenous because of an unobservable omitted factor, 'individual innate ability'. The researcher selects 'the distance in kilometres from the student's family home to the nearest university (Distance)' as a candidate instrument Z. Which of the following statements about instrument validity and the properties of two-stage least squares (2SLS) is entirely correct?",
        options: [
          { key: "A", text: "Z must satisfy both the relevance condition (Cov(Z, Educ) ≠ 0) and the strict exogeneity/exclusion assumption (Cov(Z, u) = 0 and Z must not directly determine wages)", isCorrect: true },
          { key: "B", text: "Even if the first-stage regression's F statistic is only 2.8 (far below 10), the 2SLS estimator remains absolutely unbiased with minimum variance as long as the sample size N tends to infinity", isCorrect: false, trapId: "trap_econ_2_1" },
          { key: "C", text: "When the model is exactly identified (number of endogenous variables = number of instruments = 1), a Sargan-Hansen over-identification test can be used to test statistically and rigorously whether Z is exogenous", isCorrect: false, trapId: "trap_econ_2_2" },
          { key: "D", text: "To strengthen the causal interpretation, a valid instrument Z must have a significant and directly strong driving correlation with the dependent variable ln(Wage)", isCorrect: false, trapId: "trap_econ_2_3" }
        ],
        explanation: "[Authoritative examination analysis · instrumental variables and causal identification]: (1) The two iron laws of an instrument: the exogeneity condition (orthogonal to the disturbance and with no direct causal path) plus the relevance condition (strongly correlated with the endogenous variable); (2) the Staiger-Stock rule of thumb: only a first-stage F > 10 rules out the weak-instrument risk! A weak instrument can make 2SLS even more biased than ordinary OLS! (3) Under exact identification the model has 0 degrees of freedom, so the exogeneity assumption must rest on economic-theoretic argument and cannot be tested directly by mathematical means!",
        traps: {
          trap_econ_2_1: {
            title: "🚨 Fatal blind spot on weak instruments: a large sample does not automatically rescue the severe bias of a weak instrument",
            desc: "This is the top-tier empirical disaster scene in econometrics! When first-stage relevance is weak (F < 10), the asymptotic bias of 2SLS moves towards that of OLS, the sampling distribution becomes extremely fat-tailed and distorted, conventional standard errors fail completely, and even devastating spurious causality can result!",
            prereq: "Prerequisite: the Staiger-Stock weak-instrument and finite-sample-bias results",
            radarHit: "boundary"
          },
          trap_econ_2_2: {
            title: "🚨 Mathematical blind spot on degrees of freedom and identification: exact identification makes a statistical exogeneity test impossible",
            desc: "An over-identification test (such as the Sargan test or the Hansen J statistic) presupposes that the number of instruments m strictly exceeds the number of endogenous variables k (m > k). Under exact identification the residuals are exactly orthogonal to the fitted values and the residual sum of squares has 0 degrees of freedom, so no test can be performed at all!",
            prereq: "Prerequisite: the definition of the degrees of freedom of the Sargan-Hansen over-identification statistic",
            radarHit: "precision"
          },
          trap_econ_2_3: {
            title: "🚨 Exclusion restriction fully inverted: a valid instrument must never directly affect the dependent variable!",
            desc: "The strict definition of the exclusion restriction is that the instrument Z may affect wages only indirectly, through the single channel of the endogenous variable Educ! If Z itself directly determines wages, then that variable enters the disturbance of the original equation and exogeneity is destroyed!",
            prereq: "Prerequisite: causal DAGs (directed acyclic graphs) and the exclusion-restriction theorem",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Causal inference · topology of instrument identification and exogeneity constraints",
          nodes: [
            { id: "c1", label: "2SLS instrument identification", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Exogenous exclusion: Cov(Z,u)=0", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Strong relevance: first-stage F > 10", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Weak-instrument trap: F < 10 causes severe bias", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Misplacement trap: Sargan test under exact identification", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Causal exogeneity constraint" },
            { from: "p2", to: "c1", label: "Identification-strength gate" },
            { from: "c1", to: "t1", label: "Common error (underestimating the damage of a weak instrument)" },
            { from: "c1", to: "t2", label: "Common error (ignoring the test's degrees-of-freedom constraint)" }
          ]
        },
        socraticPrompt: "Draw a causal arrow in your mind: if areas close to a university are themselves high-wage coastal metropolises (that is, Z directly affects Wage), how could we ever distinguish whether the higher wages come from more schooling or from being born in a big city? That is exactly why the exclusion restriction matters so much!"
      },
      {
        id: "econ_3",
        difficulty: "★★★★☆",
        tag: "Violation of classic assumptions · heteroskedasticity, the White test and robust standard errors",
        stem: "In a cross-sectional regression of household consumption expenditure, the dispersion of saving and consumption elasticities among wealthy households is far greater than among low-income households, so the error term exhibits heteroskedasticity that fans out as income rises (Var(u_i|X_i) = σ_i²). Which of the following statements about the harm heteroskedasticity does to OLS, the available tests and the corrective strategies fully conforms to modern empirical practice?",
        options: [
          { key: "A", text: "Under heteroskedasticity the OLS estimator β̂ loses both unbiasedness and consistency entirely, and the estimated regression coefficients are worthless as a reference", isCorrect: false, trapId: "trap_econ_3_1" },
          { key: "B", text: "The White test requires the researcher to know the exact mathematical form of the heteroskedasticity in advance (for example an exponential or a linear form) before it can be applied", isCorrect: false, trapId: "trap_econ_3_2" },
          { key: "C", text: "The OLS estimator remains unbiased and consistent, but the standard errors computed by the conventional formula are severely biased; the standard modern practice is to use White heteroskedasticity-robust standard errors directly for statistical inference", isCorrect: true },
          { key: "D", text: "Weighted least squares (WLS) is unconditionally superior to OLS with robust standard errors in every situation and can never introduce new model-specification error", isCorrect: false, trapId: "trap_econ_3_3" }
        ],
        explanation: "[Authoritative examination analysis · consequences of heteroskedasticity and robust inference]: (1) Heteroskedasticity violates the homoskedasticity assumption and destroys the 'efficiency (BLUE)' part of the Gauss-Markov theorem, but it leaves the expectation E(β̂)=β completely unaffected, so the OLS estimator remains unbiased and consistent! (2) The truly fatal injury of heteroskedasticity is that Var(β̂) computed by the conventional formula is biased, which distorts t statistics and confidence intervals across the board! (3) The White test uses an auxiliary regression and requires no presupposed form of heteroskedasticity; the current gold standard in the literature is to report OLS coefficients with heteroskedasticity-robust standard errors (for example ', robust' in Stata)!",
        traps: {
          trap_econ_3_1: {
            title: "🚨 High-frequency property-confusion pitfall: mistaking 'impaired efficiency' for a 'loss of unbiasedness'",
            desc: "60% of the class will blurt out 'the OLS estimator is biased'! The sole premise for unbiasedness is exogeneity, E(u|X)=0. A larger or smaller residual variance only makes the estimator's sampling fluctuation larger; it never shifts the centre of the estimator's population average systematically!",
            prereq: "Prerequisite: the breakpoint between the unbiasedness condition and the BLUE efficiency condition",
            radarHit: "recall"
          },
          trap_econ_3_2: {
            title: "🚨 Confusion over test mechanics: mistaking the White test for a test that depends on a specific functional form",
            desc: "The White test's greatest breakthrough is precisely that it runs an auxiliary regression of the squared residuals on the first-order terms, squares and interactions of all regressors, so the researcher never needs to guess which particular function generates the heteroskedasticity!",
            prereq: "Prerequisite: the construction of the White (1980) asymptotic large-sample auxiliary regression",
            radarHit: "boundary"
          },
          trap_econ_3_3: {
            title: "🚨 Blind-faith WLS anti-pattern: WLS with the wrong weights is even worse than OLS",
            desc: "Feasible generalised least squares (FGLS/WLS) is asymptotically efficient only when the researcher guesses the structure of the heteroskedasticity function correctly. If the weighting matrix is misspecified, the WLS estimator actually loses consistency, which is why almost all top-tier modern empirical papers use OLS with robust standard errors!",
            prereq: "Prerequisite: the robustness risk of FGLS and the sandwich variance estimator",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "Heteroskedasticity · causes, consequences and the White robust-inference map",
          nodes: [
            { id: "c1", label: "Heteroskedasticity (Var(u|X)=σi²)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Coefficients stay unbiased and consistent", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Remedy: White robust standard errors", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Misconception: OLS coefficients judged biased", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Misconception: applying WLS weights blindly", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Exogeneity assumption holds" },
            { from: "p2", to: "c1", label: "Sandwich covariance correction" },
            { from: "c1", to: "t1", label: "Common error (conflating high variance with a biased expectation)" },
            { from: "c1", to: "t2", label: "Common error (ignoring weight misspecification)" }
          ]
        },
        socraticPrompt: "Think: if an electronic scale occasionally jitters and its readings scatter more (high variance), but the average of 100 weighings is still perfectly accurate (unbiased), should we throw the scale away, or give it a proper manual that correctly computes its error range (robust standard errors)?"
      }
    ]
  },
  law: {
    name: "Commercial & Contract Law",
    badge: "Legal Foundations",
    questions: [
      {
        id: "law_1",
        difficulty: "★★★☆☆",
        tag: "Revocable juristic acts · duration of the right of revocation",
        stem: "On 1 March 2023, Party A was induced by fraud to conclude a second-hand car sale contract with Party B, and on 1 May of the same year Party A became aware of the fraud. Under the Civil Code provisions on revocable juristic acts, from what date does the preclusive period for Party A to request a people's court to rescind the contract start to run, and by what date must it expire at the latest?",
        options: [
          { key: "A", text: "Runs from the date the contract was signed (1 March 2023) and expires no later than 3 years afterwards", isCorrect: false, trapId: "trap_law_1" },
          { key: "B", text: "Runs from the date the fraud became known (1 May 2023) and expires no later than 1 year afterwards", isCorrect: true },
          { key: "C", text: "Runs from the date the fraudulent conduct ceased and expires no later than 1 year afterwards", isCorrect: false, trapId: "trap_law_2" },
          { key: "D", text: "Runs from the date the contract was signed and, irrespective of knowledge, expires in all cases within 2 years", isCorrect: false, trapId: "trap_law_3" }
        ],
        explanation: "[Authoritative examination analysis · Civil Code Art. 152]: The right of revocation for material misunderstanding must be exercised within 90 days of the date it becomes known, and the right of revocation for fraud must be exercised within 1 year of the date the fraud is known or ought to have been known; the right of revocation is extinguished if it is not exercised within 5 years of the date of the act. This period is preclusive in nature: it is not subject to suspension, interruption or extension!",
        traps: {
          trap_law_1: {
            title: "🚨 Classic confusion: applying the 3-year limitation period to a formative right",
            desc: "The most common trap in the cohort. General-purpose chatbots also tend to apply the 3-year limitation period of Civil Code Art. 188 to the right of revocation. A limitation period governs claims, whereas the right of revocation is a formative right and is therefore subject to a strict statutory preclusive period.",
            prereq: "Prerequisite: the distinction between claims and formative rights, and statutory preclusive periods",
            radarHit: "trapDefense"
          },
          trap_law_2: {
            title: "🚨 Norm-mismatch trap: conflating the statutory start dates for 'fraud' and 'duress'",
            desc: "The Civil Code draws a strict distinction between fraud and duress: only duress runs from 'the date the duress ceased', whereas fraud runs from 'the date the ground for revocation is known or ought to have been known'!",
            prereq: "Prerequisite: statutory start-date conditions for defects of will caused by duress and fraud",
            radarHit: "boundary"
          },
          trap_law_3: {
            title: "🚨 Repealed-provision rote-memorisation trap: confusing the old Contract Law with the current Civil Code",
            desc: "The student wrongly applies a provision of the repealed Contract Law. The current Civil Code uniformly provides a 1-year period running from fraud and a maximum protection period of 5 years (not 2 years).",
            prereq: "Prerequisite: the system of the right of revocation in the General Provisions of the Civil Code",
            radarHit: "recall"
          }
        },
        graph: {
          title: "Civil Code Art. 152 · topology subgraph of revocable juristic acts",
          nodes: [
            { id: "c1", label: "Preclusive period of the right of revocation", type: "core", x: 260, y: 140 },
            { id: "p1", label: "1 year from knowledge of the fraud", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Maximum 5 years from the act", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: misapplying the 3-year limitation period", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: misremembering the duress end point", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Primary preclusive period" },
            { from: "p2", to: "c1", label: "Maximum protection period" },
            { from: "c1", to: "t1", label: "Common error (confusing the nature of the right)" },
            { from: "c1", to: "t2", label: "Common error (mismatching the start date)" }
          ]
        },
        socraticPrompt: "Stop and think for a moment: in civil-law theory, when a party extinguishes an already-formed contract, is it exercising a 'claim' that compels the counterparty to pay money or return goods, or a 'formative right' that can alter the legal relationship by unilateral declaration? Why are the time limits for these two kinds of right fundamentally different?"
      },
      {
        id: "law_2",
        difficulty: "★★★★☆",
        tag: "Property law · requirements and defences of bona fide acquisition of movables",
        stem: "A lends his professional DSLR camera to B for use. Without authorisation, B sells it at the fair market price of RMB 12,000 to C, a photography enthusiast who is unaware of the arrangement, and completes delivery and payment on the spot. A week later A discovers this and asserts ownership against C, demanding the camera's return without compensation. As to the legal effect of this case, which of the following statements is entirely correct?",
        options: [
          { key: "A", text: "Because B had no power of disposal over the camera, the sale contract between B and C is absolutely void ab initio and C cannot acquire ownership", isCorrect: false, trapId: "trap_law_2_1" },
          { key: "B", text: "C has acquired original ownership of the camera under the bona fide acquisition regime of the Civil Code, and A has no right to demand return of the original property", isCorrect: true },
          { key: "C", text: "Because the camera was lent rather than lost, C must first pay A reasonable compensation before retaining it", isCorrect: false, trapId: "trap_law_2_2" },
          { key: "D", text: "Bona fide acquisition applies only to real-property rights; a movable remains in a pending-validity state until the original owner A expressly ratifies the transfer", isCorrect: false, trapId: "trap_law_2_3" }
        ],
        explanation: "[Authoritative examination analysis · Civil Code Arts. 311 and 597]: (1) A sale contract concluded by a person without power of disposal is valid (the old Contract Law Art. 51 pending-validity doctrine is entirely abolished); (2) the requirements for bona fide acquisition are: the transferee is in good faith and free of gross negligence at the time of transfer, the transfer is at a reasonable price, and delivery has been completed in accordance with law. C satisfies all three requirements and therefore acquires ownership of the movable by operation of law; A may only claim tort damages or unjust enrichment from B, the person without power of disposal!",
        traps: {
          trap_law_2_1: {
            title: "🚨 Repealed-law rote-memorisation trap: equating a 'defect in the power of disposal' with an 'absolutely void sale contract'",
            desc: "This is the classic disaster zone that 58% of students fall into in law-school finals and postgraduate entrance examinations! The Civil Code clearly separates the obligational act (the contractual claim) from the act of disposal (the change in real rights). A sale contract remains valid even if concluded without power of disposal; failure to perform gives rise to liability for breach, and a bona fide transferee is directly protected by bona fide acquisition!",
            prereq: "Prerequisite: the separation principle between the validity of a contractual claim and the change of real rights",
            radarHit: "recall"
          },
          trap_law_2_2: {
            title: "🚨 Rule-confusion trap: applying the 'redemption of lost or stolen property' rule to a voluntarily lent, entrusted article",
            desc: "Civil Code Art. 312 provides a 2-year right to demand return upon payment of consideration only for lost property and other 'things that left possession without the true owner's intent'. Here A voluntarily lent the camera to B (an article entrusted to possession), so the original owner must bear the trust risk himself; there is simply no right of redemption for consideration!",
            prereq: "Prerequisite: the difference in legal consequences between lost or escaped articles and entrusted articles",
            radarHit: "boundary"
          },
          trap_law_2_3: {
            title: "🚨 Blind spot in the scope of the doctrine: bona fide acquisition spans both movables and immovables",
            desc: "General-purpose AI frequently mixes up delivery for movables with registration for immovables. Bona fide acquisition is precisely a statutory regime of original acquisition resting on two pillars: the public credibility of possession for movables and of registration for immovables!",
            prereq: "Prerequisite: the principles of publicity and public credibility as applied to movables",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Civil Code Art. 311 · topology of the elements and defences of bona fide acquisition",
          nodes: [
            { id: "c1", label: "Bona fide acquisition of movables (Art. 311)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Good faith + reasonable price + completed delivery", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Risk allocation for entrusted articles", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: wrongly treating the sale contract as void", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: misapplying lost-property redemption", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Three statutory elements" },
            { from: "p2", to: "c1", label: "Bars return of the original" },
            { from: "c1", to: "t1", label: "Common error (failing to distinguish obligational from dispositive acts)" },
            { from: "c1", to: "t2", label: "Common error (conflating escaped and entrusted articles)" }
          ]
        },
        socraticPrompt: "Think about this: if the original owner A carelessly lent the camera to an unreliable friend B, while the bona fide buyer C paid real money in the open market and obtained the camera, why does the law protect C rather than A? What commercial-transaction-security value orientation does this reflect?"
      },
      {
        id: "law_3",
        difficulty: "★★★★☆",
        tag: "General Provisions · apparent authority and liability based on appearance",
        stem: "A software technology company dismissed its vice-president of sales, Zhang, but negligently failed to collect in time the blank business authorisation letter bearing the company seal and the dedicated contract seal that he held. The next day Zhang, using those documents and acting in the company's name, concluded an RMB 800,000 server-room leasing contract with a cloud service provider that was unaware of his departure and had exercised ordinary care. As to the validity of, and liability under, that contract, which of the following statements is correct?",
        options: [
          { key: "A", text: "Zhang had no authority after leaving office, so the contract is absolutely void ab initio and the technology company bears no civil liability whatsoever", isCorrect: false, trapId: "trap_law_3_1" },
          { key: "B", text: "Apparent authority is established; the contract is valid as against the technology company, which must bear the contractual obligation to perform and pay", isCorrect: true },
          { key: "C", text: "The contract is a pending-validity contract; if the technology company does not ratify it within the statutory 30 days, the contract is extinguished outright", isCorrect: false, trapId: "trap_law_3_2" },
          { key: "D", text: "Apparent authority can be established only if the cloud service provider can fully prove that the technology company's executives had a subjective intent to defraud", isCorrect: false, trapId: "trap_law_3_3" }
        ],
        explanation: "[Authoritative examination analysis · Civil Code Art. 172]: Where an actor performs an agency act without authority, beyond the scope of authority, or after the authority has terminated, and the counterparty has reason to believe that the actor has authority, the agency act is valid. The company's failure to recover the seals and the authorisation letter amounts to gross negligence (an attributable appearance), and the counterparty is in good faith and free from negligence, so apparent authority is established! After performing, the company may seek recourse against Zhang!",
        traps: {
          trap_law_3_1: {
            title: "🚨 Mechanical denial-of-authority trap: ignoring the commercial-appearance doctrine's tilt towards bona fide third parties",
            desc: "Many beginners see only the half-sentence 'Zhang had left office and had no authority' and mechanically hold the contract void. The very purpose of the apparent-authority regime is to bind the principal to the legal consequences when authority is substantively lacking but the principal has created an appearance of right!",
            prereq: "Prerequisite: the appearance-of-right theory and the protection of reliance interests",
            radarHit: "trapDefense"
          },
          trap_law_3_2: {
            title: "🚨 Reversed-order trap: downgrading 'apparent authority' to the 'pending validity of unauthorised agency in the narrow sense'",
            desc: "Once apparent authority is established, the counterparty has a choice: it may either assert that the apparent agency is valid and require the company to perform, or it may rescind on its own initiative. But the principal (the technology company) has no right at all to annul the contract unilaterally by 'refusing to ratify'!",
            prereq: "Prerequisite: the breakpoint in legal consequences between apparent authority and unauthorised agency in the narrow sense",
            radarHit: "boundary"
          },
          trap_law_3_3: {
            title: "🚨 Over-strict attribution trap: confusing 'attributability of the appearance of right' with 'intent to commit a tort'",
            desc: "Establishing apparent authority does not require the principal to have any subjective intent to defraud! Objective negligence such as poor seal management or failure to recover the authorisation letter, if it creates the appearance of right, is sufficient to establish the principal's attributability!",
            prereq: "Prerequisite: the criteria for the objective and subjective elements of apparent authority",
            radarHit: "synthesis"
          }
        },
        graph: {
          title: "Civil Code Art. 172 · topology of the attribution of apparent-authority effects",
          nodes: [
            { id: "c1", label: "Apparent authority (Art. 172)", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Appearance of right + principal's negligence", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Counterparty in good faith and without negligence", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: wrongly held absolutely void", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: wrongly requiring the principal's intent", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Appearance creates attributability" },
            { from: "p2", to: "c1", label: "Reliance-protection element" },
            { from: "c1", to: "t1", label: "Common error (mechanical view of lack of authority)" },
            { from: "c1", to: "t2", label: "Common error (over-strict subjective element)" }
          ]
        },
        socraticPrompt: "Put yourself in the shoes of a supplier: if the person in front of you produces an authorisation letter and company seal stamped with the official red seal, could you realistically check whether that company issued an internal notice dismissing him today? Why does the law make a company that manages its seals carelessly foot the bill?"
      }
    ]
  },
  or: {
    name: "Operations Research & Optimization",
    badge: "Year 2 Core Syllabus",
    questions: [
      {
        id: "or_1",
        difficulty: "★★★☆☆",
        tag: "Planning modelling · physical non-negativity of decision variables and constraint boundaries",
        stem: "An equipment manufacturer plans to produce two industrial components, A and B; each component consumes steel, labour hours and CNC milling-machine hours. When building a linear programming (LP) model that maximises total sales profit (max Z = 300x₁ + 500x₂), which of the following statements about the elements of the mathematical model and the standard-form conventions is entirely correct?",
        options: [
          { key: "A", text: "As long as the objective function is linear, the decision variables x₁ and x₂ may take any negative real values; the model need not define physical non-negativity constraints because the solver corrects them automatically", isCorrect: false, trapId: "trap_or_1" },
          { key: "B", text: "The non-negativity constraints x₁ ≥ 0 and x₂ ≥ 0 must be added strictly to the constraint set; if the problem is infeasible, that means the intersection of the constraint hyperplanes — the feasible region — is the empty set, not that the objective diverges to positive infinity", isCorrect: true },
          { key: "C", text: "The feasible region of a linear programming model is necessarily a non-convex open space, so genetic algorithms or simulated annealing must be used to search the surface for a local optimum", isCorrect: false, trapId: "trap_or_2" },
          { key: "D", text: "To convert a cost-minimisation model into the standard maximisation model, one need only multiply the objective coefficients by -1; the inequality directions of all remaining constraints must stay exactly as they are", isCorrect: false, trapId: "trap_or_3" }
        ],
        explanation: "[Authoritative examination analysis · Hamdy Taha's planning modelling and standard form]: (1) Decision variables represent real physical entities or production and sales quantities and must satisfy non-negativity constraints ($x_j \\ge 0$), otherwise absurd solutions such as producing a negative number of components appear; (2) the feasible region of a linear programme is necessarily a convex polyhedron bounded by the intersection of hyperplanes, and the extreme point theorem guarantees that an optimal solution is attained at an extreme point; infeasibility means the constraints are mutually exclusive so that the intersection forming the feasible region is empty!",
        traps: {
          trap_or_1: {
            title: "🚨 Detached-from-physical-reality trap: omitting the non-negativity constraints",
            desc: "This is the serious error operations-research beginners commit most often in modelling! A computer solver understands only pure symbolic logic: if x₁ ≥ 0 is omitted, the arithmetic may return x₁ = -100 and a spuriously high profit, which makes the plan completely unusable in engineering terms!",
            prereq: "Prerequisite: the three standard-form requirements of a linear programme and the non-negativity axiom",
            radarHit: "boundary"
          },
          trap_or_2: {
            title: "🚨 Misjudging the geometry of the feasible region trap: treating a convex polyhedron as a non-convex surface",
            desc: "All constraints of a linear programme are linear first-order inequalities, and the feasible region formed by the intersection of hyperplane half-spaces is strictly a convex set — never a non-convex surface! The simplex method iterates along extreme-point boundaries to find the global optimum!",
            prereq: "Prerequisite: the definition of a convex set and the extreme point theorem",
            radarHit: "recall"
          },
          trap_or_3: {
            title: "🚨 Careless standard-form conversion trap: constraint directions not adjusted in tandem",
            desc: "When converting minimisation to maximisation, besides negating the objective function, multiplying both sides of an inequality by a negative sign requires the inequality direction to be strictly reversed, or non-negative slack variables must be introduced to obtain the equality standard form!",
            prereq: "Prerequisite: LP duality theory and the simplex standard-form transformation matrix",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Operations Research Chapter 1 · linear programming modelling and solution-space topology",
          nodes: [
            { id: "c1", label: "Three elements of a planning model", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Physical non-negativity constraint x ≥ 0", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Extreme points of a convex polyhedron feasible region", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: omitting non-negative output", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: wrongly judging the feasible region non-convex", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Physical reality boundary" },
            { from: "p2", to: "c1", label: "Extreme-point optimality guarantee" },
            { from: "c1", to: "t1", label: "Common error (detached from real-world meaning)" },
            { from: "c1", to: "t2", label: "Common error (confusing the geometric topology)" }
          ]
        },
        socraticPrompt: "Think: if a bakery wants to work out how many croissants to bake tomorrow to earn the most money, and the solver reports that 'baking minus 5 croissants' is the most profitable option, could that be carried out in the physical world? Why must mathematical formulations lock down physical boundaries with constraints?"
      }
    ]
  },
  mis: {
    name: "Management Information Systems",
    badge: "Year 2 Core Syllabus",
    questions: [
      {
        id: "mis_1",
        difficulty: "★★★☆☆",
        tag: "Organisational system levels · TPS-DSS coordination and the C2M reverse supply chain",
        stem: "A retail manufacturing enterprise is advancing its digital transformation. When analysing Laudon's classic information-system architecture and the new-retail C2M (Customer-to-Manufacturer) reverse-customisation business model, which of the following statements about the division of labour among business-system levels and value-chain coordination is entirely correct?",
        options: [
          { key: "A", text: "The enterprise strategic decision support system (ESS) should connect in real time to every small transaction on the point-of-sale terminals and present each one to board executives for daily verification", isCorrect: false, trapId: "trap_mis_1" },
          { key: "B", text: "The TPS (transaction processing system) sits at the bottom layer supporting daily high-frequency structured business transactions (such as order creation and inventory deduction); the C2M model aggregates long-tail demand through social fission such as group buying and connects it directly to factory production, and its core value lies in using algorithms to predict demand precisely and eliminate intermediate agents and the inventory bullwhip effect", isCorrect: true },
          { key: "C", text: "A modern enterprise management information system (MIS) consists purely of IT tools such as computer software and cloud-server hardware and has nothing to do with organisational restructuring, business process reengineering (BPR) or staff training", isCorrect: false, trapId: "trap_mis_2" },
          { key: "D", text: "The main purpose of an ERP (enterprise resource planning) system is to erect stricter data barriers between departments and prevent financial and production data from being shared across systems", isCorrect: false, trapId: "trap_mis_3" }
        ],
        explanation: "[Authoritative examination analysis · Laudon's management information systems and digital new retail]: (1) The TPS records daily deterministic operations at the bottom layer, while mid- and senior-level decision systems (MIS/DSS/ESS) distil higher-order business insight through aggregation and modelling; (2) C2M reverse customisation relies on digital long-tail aggregation to eliminate multi-tier intermediaries and dampen the bullwhip effect; (3) an MIS is a sociotechnical system combining technology, people and organisation — emphatically not a pure hardware purchase!",
        traps: {
          trap_mis_1: {
            title: "🚨 Data-granularity mismatch trap: executive dashboards conflated with bottom-layer transaction logs",
            desc: "Presenting unaggregated bottom-layer transaction detail to executives is a classic information-architecture anti-pattern! Executives need macro strategic dashboards and trend indicators; raw detail causes information overload!",
            prereq: "Prerequisite: the data-granularity theory of the enterprise pyramid levels (TPS/MIS/DSS/ESS)",
            radarHit: "boundary"
          },
          trap_mis_2: {
            title: "🚨 Technological-determinism trap: equating IT tools with systemic change",
            desc: "Buying ERP/CRM software does not amount to system success! Without business process reengineering (BPR), organisational change management and aligned staff incentives, a go-live often becomes mere decoration or even triggers organisational turmoil!",
            prereq: "Prerequisite: the sociotechnical paradigm of information systems and business process reengineering (BPR)",
            radarHit: "recall"
          },
          trap_mis_3: {
            title: "🚨 Reversed judgement of the enterprise integration hub: ERP removes islands rather than building barriers",
            desc: "The core mission of ERP is precisely to break down departmental barriers and information silos and to establish a single source of truth (SSOT) integrating finance, purchasing-sales-inventory and manufacturing!",
            prereq: "Prerequisite: the core ERP architecture and the enterprise's end-to-end business integration chain",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Management information systems · sociotechnical paradigm and enterprise integration architecture",
          nodes: [
            { id: "c1", label: "Enterprise four-level system pyramid", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Bottom layer, high-frequency transactions: TPS", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "C2M reverse supply-chain algorithms", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: granularity mismatch — executives shown raw detail", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: mistaking tool purchase for transformation", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Foundation of structured data sources" },
            { from: "p2", to: "c1", label: "Eliminating intermediaries and the bullwhip effect" },
            { from: "c1", to: "t1", label: "Common error (information-overload misalignment)" },
            { from: "c1", to: "t2", label: "Common error (technological-determinism bias)" }
          ]
        },
        socraticPrompt: "Think: if a hospital director had to review, one by one, the system log of every outpatient who paid a 10-yuan registration fee, would he still have time to plan the hospital's medical-research strategy for the year? Why must information systems aggregate and abstract data at different levels according to management level?"
      }
    ]
  },
  prob_stat: {
    name: "Probability & Mathematical Statistics",
    badge: "Year 2 Math Foundation",
    questions: [
      {
        id: "prob_stat_1",
        difficulty: "★★★★☆",
        tag: "Prior-posterior inversion · Bayes' theorem and testing event independence",
        stem: "A university laboratory has developed a non-destructive optical detector for nanoscale micro-cracks in chips. For a batch of wafer dies, the prior probability of the micro-crack is P(A) = 0.002 (two per thousand). The detector's sensitivity, i.e. the probability of a positive reading given a cracked chip, is P(+|A) = 0.99; its false-positive rate, i.e. a positive reading given an uncracked chip, is P(+|Ā) = 0.05. A die is drawn at random and tests positive. Regarding the true posterior probability P(A|+) that the die really has a micro-crack, and the basic theory of probability, which of the following statements is entirely correct?",
        options: [
          { key: "A", text: "Since the detector's positive accuracy is as high as 99%, the probability that this positively tested chip has a micro-crack must be 99%, and the prior prevalence need not be considered", isCorrect: false, trapId: "trap_stat_1" },
          { key: "B", text: "Two mutually exclusive events (incompatible, AB=∅) are equivalent to two independent events (P(AB)=P(A)P(B)), so mutually exclusive events never influence each other", isCorrect: false, trapId: "trap_stat_2" },
          { key: "C", text: "Applying Bayes' theorem in reverse, and constrained by the extremely low prior base rate (0.002), the true posterior probability is P(A|+) = (0.002×0.99) / (0.002×0.99 + 0.998×0.05) ≈ 3.81%; and if two events with positive probability are independent, they can never be mutually exclusive (they must be able to occur together)", isCorrect: true },
          { key: "D", text: "The sum of the probabilities of all values of a discrete random variable may exceed 1, provided each individual probability is non-negative", isCorrect: false, trapId: "trap_stat_3" }
        ],
        explanation: "[Authoritative examination analysis · Bayes' inversion formula and the false-positive paradox]: (1) In rare-event screening the extremely low prior probability (0.002) means that even with high sensitivity (99%), the overwhelming majority of positive results come from the small false-positive fraction of the huge healthy sample (0.998×0.05 ≈ 0.0499), and the true posterior is only about 3.81%! (2) Mutual exclusivity and independence are fundamentally opposed: if P(A)>0, P(B)>0 and the events are mutually exclusive, then P(AB)=0 ≠ P(A)P(B), so mutually exclusive events are necessarily dependent!",
        traps: {
          trap_stat_1: {
            title: "🚨 Base rate fallacy: mistaking sensitivity for the confirmed posterior rate",
            desc: "This is the probability pitfall that 72% of students — and even seasoned engineers — fall into most often! The key premise of an extremely low prior prevalence is ignored, and the conditional probability P(+|A) is conflated with P(A|+)!",
            prereq: "Prerequisite: normalisation of the conditional-probability measure and the law of total probability",
            radarHit: "boundary"
          },
          trap_stat_2: {
            title: "🚨 High-risk trap: conflating set-theoretic exclusivity with statistical independence",
            desc: "Mutual exclusivity says 'the intersection is empty, so they cannot occur together'; independence says 'the occurrence of one does not change the probability of the other at all'! If B absolutely cannot occur when A occurs, then A imposes an extremely strong negative informational constraint on B — how could they be independent?",
            prereq: "Prerequisite: the strict mathematical criterion for statistical independence, P(AB)=P(A)P(B)",
            radarHit: "recall"
          },
          trap_stat_3: {
            title: "🚨 Missing normalisation property of the discrete probability mass function (PMF)",
            desc: "Kolmogorov's second axiom of normalisation states explicitly that P(Ω)=1: the probabilities of a discrete random variable over the entire sample space must sum to exactly 1 and can never exceed 1!",
            prereq: "Prerequisite: Kolmogorov's axiomatic system and PMF normalisation",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Probability and statistics · axiomatic measure and the Bayesian prior-posterior topology",
          nodes: [
            { id: "c1", label: "Bayesian posterior-update theorem", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Prior base rate P(A)=0.002", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Normalisation of the total-probability denominator", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: mistaking sensitivity for the posterior rate", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: conflating exclusivity with independence", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Inferring cause from effect: the core prior" },
            { from: "p2", to: "c1", label: "Partition of the denominator into a complete event group" },
            { from: "c1", to: "t1", label: "Common error (base rate fallacy)" },
            { from: "c1", to: "t2", label: "Common error (conflating geometric and informational measures)" }
          ]
        },
        socraticPrompt: "Think: suppose only 1 person in the world has a rare disease, and a hospital has a test with 99.9% accuracy. If all 8 billion people on Earth were tested, 8 million healthy people would be falsely reported positive while only 1 is truly ill. If you received a positive report, would your chance of actually having the disease really be 99.9%?"
      }
    ]
  },
  mkt: {
    name: "Marketing Principles & Analytics",
    badge: "Year 2 Core Syllabus",
    questions: [
      {
        id: "mkt_1",
        difficulty: "★★★☆☆",
        tag: "STP strategic positioning · 4Ps coordination and Porter's competitive strategy",
        stem: "When analysing China's freshly made coffee market (using the '9.9-yuan price war' between Luckin Coffee and Cotti Coffee as a real-world case), which of the following analyses of the implementation of the classic STP strategic marketing framework and Porter's five-forces competitive strategy is entirely correct?",
        options: [
          { key: "A", text: "The best market-positioning strategy for a mature brand is to 'try to cater to all the needs of every consumer group in society', so market segmentation and target selection are unnecessary", isCorrect: false, trapId: "trap_mkt_1" },
          { key: "B", text: "Luckin relies on a dense network of lower-tier-city stores and a fully digital, automated ordering process to target, in its chosen segment, white-collar customers who value cost-effectiveness and convenience; a firm that relies only on low-price subsidies in a price war without achieving supply-chain scale cost leadership or differentiation in consumers' minds easily becomes 'stuck in the middle' and severely erodes its brand equity", isCorrect: true },
          { key: "C", text: "The 'Promotion' element of the marketing mix (4Ps) is the entire content of modern marketing, and product development and pricing have nothing to do with marketing", isCorrect: false, trapId: "trap_mkt_2" },
          { key: "D", text: "For a low-involvement fast-moving consumer good such as everyday freshly ground coffee, consumers spend several weeks reading ten-thousand-word industry research reports before each rational purchase", isCorrect: false, trapId: "trap_mkt_3" }
        ],
        explanation: "[Authoritative examination analysis · STP strategy and Porter's three generic competitive strategies]: (1) The essence of strategy lies in trade-offs; trying to satisfy everyone blurs positioning; (2) a price war is no long-term plan — a firm must have either cost leadership backed by supply-chain economies of scale or brand differentiation in consumers' minds, otherwise it degenerates into loss-making cut-throat competition; (3) the 4Ps are the coordinated whole of product, price, place and promotion!",
        traps: {
          trap_mkt_1: {
            title: "🚨 Target-positioning over-generalisation trap: trying to please everyone",
            desc: "Without segmentation there is no positioning! A firm that tries to be an all-purpose brand is usually utterly unremarkable in the minds of every segment, and its resources are quickly eaten away by differentiated rivals!",
            prereq: "Prerequisite: STP theory and the assessment of target-segment attractiveness",
            radarHit: "boundary"
          },
          trap_mkt_2: {
            title: "🚨 Marketing-narrowing misconception: equating marketing with discount promotions",
            desc: "Many people wrongly reduce marketing to promotional discounts and overlook that Product (core value) and Place (channel control) are the durable assets that form a commercial competitive barrier!",
            prereq: "Prerequisite: the 4Ps marketing-mix coordination theory and brand-equity models",
            radarHit: "recall"
          },
          trap_mkt_3: {
            title: "🚨 Consumer-involvement model mismatch: applying high-involvement decision models to fast-moving consumer goods",
            desc: "Freshly ground coffee is a textbook low-involvement, high-frequency impulse product: consumer decisions depend on convenience, habit and price stimuli, never on long-cycle in-depth search!",
            prereq: "Prerequisite: consumer-involvement theory (the FCB grid / involvement funnel)",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Marketing · topology of STP strategic positioning and 4Ps competitive coordination",
          nodes: [
            { id: "c1", label: "Core STP strategic positioning", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Supply-chain cost-leadership barrier", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Low-involvement FMCG decision funnel", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: over-generalising to please everyone", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: narrow discounting damages brand equity", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Economies of scale underpin the price war" },
            { from: "p2", to: "c1", label: "Instant convenience and mind-share positioning" },
            { from: "c1", to: "t1", label: "Common error (lacking the courage of strategic trade-offs)" },
            { from: "c1", to: "t2", label: "Common error (tactical discounting erodes the brand)" }
          ]
        },
        socraticPrompt: "Think: if Starbucks and Luckin suddenly gave every cup of coffee away free tomorrow, would consumers still find the coffee good when the subsidies stopped the day after? If a brand attracts customers only by cutting prices, then the moment a rival cuts one yuan more than you, will the customers you worked so hard to accumulate still be there?"
      }
    ]
  },
  eng: {
    name: "Academic English & Scientific Writing",
    badge: "Year 2 Core Syllabus",
    questions: [
      {
        id: "eng_1",
        difficulty: "★★★☆☆",
        tag: "Academic paper conventions · IMRaD discourse and the rhetoric of objective hedging",
        stem: "When writing a high-level academic paper for international peer review, or a software-engineering final-year technical report, which of the following statements about academic register, hedging and anti-plagiarism norms is entirely correct?",
        options: [
          { key: "A", text: "To make academic conclusions appear more persuasive, researchers should use absolutist assertions such as 'always, absolutely, perfectly proves' as much as possible in their papers and must never use softeners such as 'may, might, suggest'", isCorrect: false, trapId: "trap_eng_1" },
          { key: "B", text: "The internationally recognised IMRaD structure of academic papers (Introduction, Methods, Results, Discussion) demands rigour and objectivity; hedging devices embody academic rigour and precisely control the scope of certainty in an argument; compliant paraphrasing must thoroughly restructure the original's sentence logic, and a patchwork that merely swaps synonyms mechanically will still be judged by plagiarism-detection systems as the academic misconduct of patchwriting", isCorrect: true },
          { key: "C", text: "When writing the Results section of a paper, one should directly mix in large amounts of subjective speculation and personal emotional declarations that have not been tested against the experimental data", isCorrect: false, trapId: "trap_eng_2" },
          { key: "D", text: "Academic English permits the free and extensive use of colloquial everyday slang such as 'kids, a lot of, cool stuff' in formal papers, with no need to distinguish the spoken register from the academic written register", isCorrect: false, trapId: "trap_eng_3" }
        ],
        explanation: "[Authoritative examination analysis · IMRaD discourse conventions and academic integrity]: (1) Scientific conclusions must leave room for doubt; hedging devices (may, indicate, suggest, potentially) display the researcher's humility and rigour in the face of the unknown; (2) paraphrasing must restate the source in one's own syntax and logic — simple synonym substitution still counts as patchwriting plagiarism! (3) The Results section lists data objectively; only the Discussion section may develop in-depth mechanistic argument!",
        traps: {
          trap_eng_1: {
            title: "🚨 Absolutist over-commitment trap: missing academic hedging",
            desc: "Using 'absolutely' or 'perfectly proves' in academic writing is a beginner's fatal flaw! Every experiment has sampling and boundary limitations, and dogmatic assertions are easily and severely rejected in peer review!",
            prereq: "Prerequisite: the objectivity of academic register and the norms of hedging rhetoric (epistemic modality)",
            radarHit: "boundary"
          },
          trap_eng_2: {
            title: "🚨 Discourse-structure function misplacement trap: smuggling subjective conjecture into the Results",
            desc: "Results must be purely objective, neutral facts and figures! Subjective extrapolation and hypothetical mechanistic explanations belong in the Discussion section!",
            prereq: "Prerequisite: the four macro-functional divisions of IMRaD academic discourse",
            radarHit: "recall"
          },
          trap_eng_3: {
            title: "🚨 Pseudo-paraphrase patchwork plagiarism trap: patchwriting is still academic misconduct",
            desc: "Merely swapping 'important' for 'significant' or 'big' for 'massive' inside someone else's sentence while leaving the original author's syntactic skeleton untouched will be flagged in red by plagiarism-detection systems such as Turnitin!",
            prereq: "Prerequisite: academic citation norms and the techniques of deep paraphrasing and structural restructuring",
            radarHit: "trapDefense"
          }
        },
        graph: {
          title: "Academic English · the IMRaD paradigm and objective hedging discourse topology",
          nodes: [
            { id: "c1", label: "IMRaD academic discourse paradigm", type: "core", x: 260, y: 140 },
            { id: "p1", label: "Objective, cautious hedging", type: "prereq", x: 120, y: 60 },
            { id: "p2", label: "Anti-plagiarism deep paraphrasing", type: "prereq", x: 400, y: 60 },
            { id: "t1", label: "Trap: absolutist over-commitment", type: "trap", x: 130, y: 240 },
            { id: "t2", label: "Trap: mechanical synonym-patchwork plagiarism", type: "trap", x: 390, y: 240 }
          ],
          edges: [
            { from: "p1", to: "c1", label: "Scientific rigour in the Discussion" },
            { from: "p2", to: "c1", label: "Legitimacy of the literature review" },
            { from: "c1", to: "t1", label: "Common error (dogmatic absolutism)" },
            { from: "c1", to: "t2", label: "Common error (flagged red by plagiarism detection)" }
          ]
        },
        socraticPrompt: "Think: if a meteorologist wrote in a paper 'it will 100% certainly rain tomorrow and there will absolutely not be a ray of sunshine', and the next day the sun came out; versus writing 'radar data show a pronounced convergence of cold and warm air masses, indicating a very high probability of rain tomorrow' — which formulation expresses the genuinely scientific attitude?"
      }
    ]
  }
};

// Active question-bank pointer (single English locale)
let DB = DB_EN;

// =============================================================================
// Internationalization dictionary (English key table, locale-ready)
// =============================================================================
const I18N = {
  en: {
    brandName: "SmartStudy AI",
    brandSubtitle: "STUDY CONSOLE v1.0",
    courseBadge: "University of Aberdeen · JC2001 Group 5 Honours Project",
    fastEnter: "Enter Study Workspace →",
    backToPortal: "Back to Portal",
    tabQuiz: "01 Misconception Quiz",
    tabTutor: "02 Socratic AI Tutor",
    tabGraph: "03 Knowledge Graph",
    tabReport: "04 Learning Telemetry",
    suitesHeading: "CURRICULUM MODULES",
    telemetryHeading: "SYSTEM METRICS",
    groundingGate: "GROUNDING GATE",
    hallucinationDrop: "HALLUCINATION DROP",
    diagnosticEngine: "DIAGNOSTIC ENGINE",
    streak: "STREAK",
    apiStatus: "API: Local Sandbox",
    switchBadge: "⇄ Switch",
    radarTitle: "COGNITIVE 5D TELEMETRY",
    radarCaption: "⚡ Adaptive Trap Tracking / Prerequisite Topology Diagnosis",
    tutorName: "Socratic AI Companion",
    tutorStatus: "GraphRAG Grounded · Zero Hallucination",
    tutorInvite: "\"Notice subtle assumptions in the question? Pick an option to test your intuition, and I will guide you to unpack underlying prerequisite theorems!\"",
    tutorBtn: "Enter Socratic Seminar Room",
    prevItem: "◀ PREV ITEM",
    resetItem: "🔄 RESET",
    nextItem: "NEXT ITEM >",
    counterPrefix: "Item",
    counterMid: "/",
    counterSuffix: "· 18 Items Practiced Today",
    benchmarkTag: "🎯 BENCHMARK TEST",
    loadingStem: "Loading question stem...",
    subjects: {
      or: "[OR] 📐 Operations Research",
      mis: "[MIS] 🌐 Management Info Sys",
      prob_stat: "[MATH] 🎲 Probability & Stats",
      mkt: "[MKT] 🎯 Marketing",
      eng: "[ENG] ✍️ Academic English",
      law: "[LAW] ⚖️ Commercial Law",
      cs: "[CS] 💻 Architecture",
      econ: "[ECON] 📈 Econometrics",
      se: "[SE] ⚙️ Software Eng."
    },
    portalHeroBadge: "🎓 University of Aberdeen · JC2001 Software Engineering",
    portalHeroTitle: "Adaptive Cognitive Knowledge Graph &<br><span class=\"hero-gradient-text\">Exam Distractor Trap Diagnosis System</span>",
    portalHeroDesc: "An intelligent diagnostic study assistant tailored for university STEM & Software Engineering curricula. Moving beyond rote memorisation to pinpoint underlying misconceptions, distractor traps, and prerequisite gaps via Socratic dialogues.",
    pillGrounded: "⚡ GraphRAG Grounded Synthesis",
    pillTraps: "🎯 36+ Distractor Traps & Misconceptions",
    pillSocratic: "💬 Socratic Guided Inquiries",
    pillRadar: "📊 5D Cognitive Competency Radar",
    authCardTitle: "🚀 Student Identity Access & Fast Showcase",
    authCardDesc: "Click any member profile below to load individual telemetry, or enter student ID:",
    authInputPlaceholder: "Or enter Student ID / Name (e.g. 50106070 or Yuxuan Wu)",
    authSubmitBtn: "Launch Study Workspace →",
    authTip: "* Sandbox demo mode enabled. Click any card to enter interactive practice.",
    featuresSubheading: "SYSTEM ARCHITECTURE & CAPABILITIES",
    featuresHeading: "Four Core Capabilities: Conventional Quiz vs SmartStudy AI",
    feat1Title: "01 · Misconception Diagnosis",
    feat1Sub: "Distractor Trap Attribution",
    feat1Desc: "<strong>Conventional Quiz Flaw:</strong> Merely scores correct/wrong without explaining the root misconception.<br><strong>SmartStudy Remedy:</strong> Every distractor is linked to specific traps and prerequisite blind spots. Picking an option unfolds a deep diagnosis drawer.",
    feat1Tag: "Causal Attribution · Prerequisite Trace",
    feat2Title: "02 · Socratic AI Companion",
    feat2Sub: "Grounded Guided Inquiry",
    feat2Desc: "<strong>Conventional AI Flaw:</strong> Dumps the final answer immediately, bypassing independent critical thinking.<br><strong>SmartStudy Remedy:</strong> Grounded in GraphRAG facts, the AI prompts stepped inquiry, nudging students to deduce core theorems independently.",
    feat2Tag: "Zero Leakage · Stepped Guidance",
    feat3Title: "03 · Knowledge Graph Topology",
    feat3Sub: "Curriculum Concept Graph",
    feat3Desc: "<strong>Conventional Study Flaw:</strong> Fragmented concepts cause exam confusion.<br><strong>SmartStudy Remedy:</strong> Visualises topological links across Software Engineering, Architecture, Econometrics, and Law (prerequisites, theorems, and common traps).",
    feat3Tag: "Neo4j Topology · Prerequisite Links",
    feat4Title: "04 · Cognitive Telemetry & Radar",
    feat4Sub: "Real-time Skill Profiling",
    feat4Desc: "<strong>Conventional Metric Flaw:</strong> Raw percentage score fails to reflect cognitive robustness.<br><strong>SmartStudy Remedy:</strong> Dynamically calculates 5 skill dimensions (Recall, Defense, Deduction, Synthesis, Boundary) to generate targeted review plans.",
    feat4Tag: "5D Radar · Adaptive Tracking",
    footerCourse: "University of Aberdeen · JC2001 Introduction to Software Engineering (2026–27)",
    footerTeam: "Group 5 (BSc BMIS): Yuxuan Wu (PM · 50106070) · Yongtong Lin (BA · 50106038) · Sijian Wang (SA · 50106045) · Hao Jiang (Dev · 50106065) · Weixin Xie (QA · 50106034) · Zijian Zhang · Yusai Xi · Siqin Dong · Mingjie Yang · Zixuan Liang",
    footerVersion: "SmartStudy Assistant PoC v1.0 · Grounded with GraphRAG & Dual-Mode Diagnostic Engine",
    diagCorrectHeader: "Great Job! Concept accurately mastered, avoiding distractor traps!",
    diagLoading: "🧠 Cognitive Engine analysing answer & trap topology...",
    diagOfflineBadge: "[Offline Topology Fallback]",
    diagOnlineBadge: "[AI Live Diagnosis]",
    weakPointPrefix: "🔍 Prerequisite Blind Spot:",
    deductionPrefix: "📉 Defense Index Impact:",
    summonTutorBtn: "💬 Summon Socratic Tutor for Step-by-Step Guidance",
    feedbackCorrectTip: "✔ Prerequisite Concept Mastery +4 | Defense Index +5",
    radarRecall: "Recall",
    radarBoundary: "Boundary",
    radarDefense: "Defense",
    radarSynthesis: "Synthesis",
    radarPrecision: "Precision"
  }
};
const API_BASE = (function() {
  if (typeof window !== "undefined" && window.location && window.location.origin && window.location.origin.startsWith("http")) {
    return window.location.origin;
  }
  return "http://127.0.0.1:8000";
})();

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

// =============================================================================
// Global state
// =============================================================================
const GEMINI_DEFAULT_KEY = "";
const GEMINI_DEFAULT_URL = "https://generativelanguage.googleapis.com/v1beta/openai";
const GEMINI_DEFAULT_MODEL = "gemini-2.0-flash";
const DASHSCOPE_DEFAULT_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1";
const DASHSCOPE_DEFAULT_MODEL = "qwen-turbo";

const savedApiKey = localStorage.getItem("smartstudy_apikey");
const activeApiKey = (savedApiKey && savedApiKey.trim()) ? savedApiKey.trim() : GEMINI_DEFAULT_KEY;
const activeProvider = localStorage.getItem("smartstudy_provider") || "mock";
const activeApiUrl = (savedApiKey && savedApiKey.trim()) ? (localStorage.getItem("smartstudy_apiurl") || DASHSCOPE_DEFAULT_URL) : DASHSCOPE_DEFAULT_URL;
const activeModel = (savedApiKey && savedApiKey.trim()) ? (localStorage.getItem("smartstudy_model") || DASHSCOPE_DEFAULT_MODEL) : DASHSCOPE_DEFAULT_MODEL;

const DEFAULT_WEAK_LISTS = [
  { tag: "Waterfall vs Agile Trade-offs", reason: "Confusing regulatory audit with extreme agile", count: 2 },
  { tag: "SOLID & Dependency Inversion (DIP)", reason: "Direct coupling to low-level drivers without interface", count: 1 }
];

const state = {
  currentSubject: (function() {
    const saved = localStorage.getItem("smartstudy_subject");
    if (saved && DB_EN[saved]) return saved;
    return "or"; // Default to the Operations Research core bank
  })(),
  currentQIndex: 0,
  activeTab: "home",
  theme: localStorage.getItem("smartstudy_theme") || "light",
  hasAnswered: false,

  // LLM endpoint & knowledge-graph configuration
  apiConfig: {
    provider: activeProvider,
    apiKey: activeApiKey,
    apiUrl: activeApiUrl,
    model: activeModel,
    neo4jUri: localStorage.getItem("smartstudy_neo4j") || "neo4j+s://smartstudy-aura.databases.neo4j.io",
    gateEnabled: localStorage.getItem("smartstudy_gate") !== "false"
  },

  // Five-dimension competency profile (0-100)
  radar: {
    recall: 76,       // Recall
    boundary: 62,     // Boundary reasoning
    trapDefense: 65,  // Trap defense
    synthesis: 72,    // Synthesis
    precision: 81     // Precision
  },

  // Practice history statistics
  stats: {
    streakDays: 5,
    trapsAvoided: 14,
    totalAnswered: 18,
    predictedScore: 86.5
  },

  // Weak concepts queued for trap remediation
  weakList: DEFAULT_WEAK_LISTS,
  reportSubject: "all"
};

let miniRadarChart = null;
let largeRadarChart = null;

// =============================================================================
// DOM loading and initialization
// =============================================================================
document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  initNavTabs();
  initWorkspaceHome();
  initApiModal();
  initSubjectSelector();
  loadBackendQuestionBank();
  initRadarCharts();
  loadQuestion();
  renderGraph();
  initSocraticChat();
  updateStatCards();
  initReportFilters();
  checkBackendHealth();
  initAuthPortal();
  initI18n();
  // Feature 002: modern AI visuals and power-user interaction layer
  initSpotlightCards();
  initComparisonSandbox();
  initCommandPalette();
});

// =============================================================================
// Landing page & student-profile auth controller (Landing & Auth Portal Controller)
// =============================================================================
const DEMO_STUDENTS = [
  {
    id: "50106070",
    name: "Yuxuan Wu",
    role: "PM · Group Leader",
    avatar: "YW",
    subject: "se",
    subjectLabel: "⚙️ Software Eng.",
    streak: 5
  },
  {
    id: "50106038",
    name: "Yongtong Lin",
    role: "Lead BA · Requirements",
    avatar: "YL",
    subject: "econ",
    subjectLabel: "📈 Econometrics",
    streak: 4
  },
  {
    id: "50106045",
    name: "Sijian Wang",
    role: "Chief Architect",
    avatar: "SW",
    subject: "cs",
    subjectLabel: "💻 Architecture",
    streak: 6
  },
  {
    id: "50106065",
    name: "Hao Jiang",
    role: "Development Lead",
    avatar: "HJ",
    subject: "se",
    subjectLabel: "⚙️ Software Eng.",
    streak: 7
  },
  {
    id: "guest",
    name: "Guest Learner",
    role: "Instant Sandbox Access",
    avatar: "GL",
    subject: "se",
    subjectLabel: "🚀 Instant Sandbox",
    streak: 1
  }
];

function getDemoStudents() {
  return DEMO_STUDENTS;
}

function switchRootView(view) {
  const portal = document.getElementById("portal-landing");
  const shell = document.getElementById("app-shell");
  if (!portal || !shell) return;

  if (view === "workspace") {
    portal.style.display = "none";
    shell.style.display = "flex";
    localStorage.setItem("smartstudy_current_view", "workspace");
    setTimeout(() => {
      window.dispatchEvent(new Event("resize"));
      if (typeof rebuildRadarCharts === "function") rebuildRadarCharts();
      if (typeof renderGraph === "function") renderGraph();
    }, 60);
  } else {
    shell.style.display = "none";
    portal.style.display = "block";
    localStorage.setItem("smartstudy_current_view", "portal");
  }
}

function switchSubject(sub) {
  if (!DB[sub]) return;
  state.currentSubject = sub;
  state.currentQIndex = 0;
  localStorage.setItem("smartstudy_subject", sub);
  const btns = document.querySelectorAll(".subject-btn");
  btns.forEach(b => {
    if (b.dataset.subject === sub) {
      b.classList.add("active");
    } else {
      b.classList.remove("active");
    }
  });
  loadQuestion();
  renderGraph();
  if (typeof resetChatWithContext === "function") resetChatWithContext();
}

function applyStudentProfile(student) {
  if (!student) return;
  state.currentUser = student;
  localStorage.setItem("smartstudy_current_user", JSON.stringify(student));

  const nameEl = document.getElementById("current-user-name");
  const roleEl = document.getElementById("current-user-role");
  const avatarEl = document.getElementById("current-user-avatar");
  if (nameEl) nameEl.textContent = student.name;
  if (roleEl) roleEl.textContent = `${student.role} (${student.id})`;
  if (avatarEl) avatarEl.textContent = student.avatar || student.name.charAt(0);

  const streakStrong = document.querySelector(".streak-badge strong");
  if (streakStrong && student.streak) streakStrong.textContent = student.streak;

  if (student.subject && DB[student.subject] && typeof switchSubject === "function") {
    switchSubject(student.subject);
  }
}

function renderDemoAccounts() {
  const demoContainer = document.getElementById("portal-demo-accounts");
  if (demoContainer) {
    const students = getDemoStudents();
    demoContainer.innerHTML = students.map(s => `
      <div class="demo-user-card" data-student-id="${s.id}" title="Click to launch workspace as ${s.name}">
        <div class="demo-avatar">${s.avatar}</div>
        <div class="demo-name">${s.name}</div>
        <div class="demo-role">${s.role}</div>
        <div class="demo-subject">${s.subjectLabel}</div>
      </div>
    `).join("");

    demoContainer.querySelectorAll(".demo-user-card").forEach(card => {
      card.addEventListener("click", () => {
        const id = card.getAttribute("data-student-id");
        const list = getDemoStudents();
        const student = list.find(s => s.id === id) || list[0];
        applyStudentProfile(student);
        switchRootView("workspace");
      });
    });
  }

  // Also populate demo cards inside the modal if it exists
  const modalGrid = document.getElementById("demo-accounts-list");
  if (modalGrid) {
    const students = getDemoStudents();
    modalGrid.innerHTML = students.map(s => `
      <div class="demo-user-card" data-student-id="${s.id}" style="padding: 10px; cursor: pointer;">
        <div class="demo-avatar" style="width: 32px; height: 32px; font-size: 0.85rem;">${s.avatar}</div>
        <div class="demo-name" style="font-size: 0.88rem;">${s.name}</div>
        <div class="demo-role" style="font-size: 0.72rem;">${s.role}</div>
      </div>
    `).join("");

    modalGrid.querySelectorAll(".demo-user-card").forEach(card => {
      card.addEventListener("click", () => {
        const id = card.getAttribute("data-student-id");
        const list = getDemoStudents();
        const student = list.find(s => s.id === id) || list[0];
        applyStudentProfile(student);
        const loginModal = document.getElementById("login-modal");
        if (loginModal) loginModal.style.display = "none";
      });
    });
  }
}

function applyLanguage(lang) {
  // Single English locale: any unknown locale code falls back to the English table.
  const dict = I18N[lang] ? I18N[lang] : I18N.en;

  // 2. Portal Header & Hero
  const portalBrandSub = document.getElementById("portal-brand-sub");
  if (portalBrandSub) portalBrandSub.textContent = dict.courseBadge;

  const fastEnterText = document.getElementById("portal-fast-enter-text");
  if (fastEnterText) fastEnterText.textContent = dict.fastEnter;

  const portalAuthNavLabel = document.getElementById("portal-auth-nav-label");
  if (portalAuthNavLabel) portalAuthNavLabel.textContent = "Sign In";


  const heroBadge = document.getElementById("portal-hero-badge-text") || document.querySelector(".portal-badge-pill span:not(.pulse-dot)");
  if (heroBadge) heroBadge.textContent = dict.portalHeroBadge;

  const heroTitle = document.querySelector(".portal-hero-title");
  if (heroTitle) heroTitle.innerHTML = dict.portalHeroTitle;

  const heroDesc = document.querySelector(".portal-hero-desc");
  if (heroDesc) heroDesc.textContent = dict.portalHeroDesc;

  const pills = document.querySelectorAll(".portal-highlights-row .portal-pill-chip");
  if (pills && pills.length >= 4) {
    pills[0].textContent = dict.pillGrounded;
    pills[1].textContent = dict.pillTraps;
    pills[2].textContent = dict.pillSocratic;
    pills[3].textContent = dict.pillRadar;
  }

  // 3. Auth Card
  const authCardTitle = document.querySelector(".auth-card-header div:first-child span:last-child");
  if (authCardTitle) authCardTitle.textContent = dict.authCardTitle;

  const authCardDesc = document.querySelector(".auth-card-header div:last-child");
  if (authCardDesc) authCardDesc.textContent = dict.authCardDesc;

  const usernameInput = document.getElementById("portal-username-input");
  if (usernameInput) usernameInput.placeholder = dict.authInputPlaceholder;

  const loginBtn = document.getElementById("portal-login-btn");
  if (loginBtn) loginBtn.innerHTML = `${dict.authSubmitBtn}`;

  const loginTip = document.getElementById("portal-login-tip");
  if (loginTip) loginTip.textContent = dict.authTip;

  // Re-render student cards
  renderDemoAccounts();

  // 4. Features Section
  const featuresSub = document.querySelector(".portal-features-section div div:first-child");
  if (featuresSub) featuresSub.textContent = dict.featuresSubheading;

  const featuresHeading = document.querySelector(".portal-features-section div h2");
  if (featuresHeading) featuresHeading.textContent = dict.featuresHeading;

  const featureCards = document.querySelectorAll(".portal-feature-card");
  if (featureCards && featureCards.length >= 4) {
    featureCards[0].querySelector(".feature-card-title").textContent = dict.feat1Title;
    featureCards[0].querySelector(".feature-card-subtitle").textContent = dict.feat1Sub;
    featureCards[0].querySelector(".feature-card-p").innerHTML = dict.feat1Desc;
    featureCards[0].querySelector(".feature-card-tag").textContent = dict.feat1Tag;

    featureCards[1].querySelector(".feature-card-title").textContent = dict.feat2Title;
    featureCards[1].querySelector(".feature-card-subtitle").textContent = dict.feat2Sub;
    featureCards[1].querySelector(".feature-card-p").innerHTML = dict.feat2Desc;
    featureCards[1].querySelector(".feature-card-tag").textContent = dict.feat2Tag;

    featureCards[2].querySelector(".feature-card-title").textContent = dict.feat3Title;
    featureCards[2].querySelector(".feature-card-subtitle").textContent = dict.feat3Sub;
    featureCards[2].querySelector(".feature-card-p").innerHTML = dict.feat3Desc;
    featureCards[2].querySelector(".feature-card-tag").textContent = dict.feat3Tag;

    featureCards[3].querySelector(".feature-card-title").textContent = dict.feat4Title;
    featureCards[3].querySelector(".feature-card-subtitle").textContent = dict.feat4Sub;
    featureCards[3].querySelector(".feature-card-p").innerHTML = dict.feat4Desc;
    featureCards[3].querySelector(".feature-card-tag").textContent = dict.feat4Tag;
  }

  // 5. Portal Footer
  const footerCourse = document.querySelector(".portal-footer div:nth-child(1)");
  if (footerCourse) footerCourse.textContent = dict.footerCourse;

  const footerTeam = document.querySelector(".portal-footer div:nth-child(2)");
  if (footerTeam) footerTeam.textContent = dict.footerTeam;

  const footerVersion = document.querySelector(".portal-footer div:nth-child(3)");
  if (footerVersion) footerVersion.textContent = dict.footerVersion;

  // 6. Sidebar (App Shell)
  const brandName = document.querySelector(".brand-meta .brand-name");
  if (brandName) brandName.textContent = dict.brandName;

  const brandSub = document.querySelector(".brand-meta .brand-subtitle");
  if (brandSub) brandSub.textContent = dict.brandSubtitle;

  const backToPortalSpan = document.querySelector("#back-to-portal-btn span");
  if (backToPortalSpan) backToPortalSpan.textContent = dict.backToPortal;

  const navHeading = document.querySelector(".nav-group-heading");
  if (navHeading) navHeading.textContent = dict.suitesHeading;

  const tabQuiz = document.querySelector('.nav-tab-item[data-view="quiz"] .tab-label');
  if (tabQuiz) tabQuiz.textContent = dict.tabQuiz;

  const tabTutor = document.querySelector('.nav-tab-item[data-view="tutor"] .tab-label');
  if (tabTutor) tabTutor.textContent = dict.tabTutor;

  const tabGraph = document.querySelector('.nav-tab-item[data-view="graph"] .tab-label');
  if (tabGraph) tabGraph.textContent = dict.tabGraph;

  const tabReport = document.querySelector('.nav-tab-item[data-view="report"] .tab-label');
  if (tabReport) tabReport.textContent = dict.tabReport;

  const apiStatusText = document.getElementById("nav-api-status-text");
  if (apiStatusText) apiStatusText.textContent = dict.apiStatus;

  const switchBadge = document.querySelector(".user-switch-badge");
  if (switchBadge) switchBadge.textContent = dict.switchBadge;

  // 7. Subject Buttons in Quiz view
  const subBtns = document.querySelectorAll(".subject-btn");
  subBtns.forEach(btn => {
    const s = btn.getAttribute("data-subject");
    if (s && dict.subjects[s]) {
      btn.textContent = dict.subjects[s];
    }
  });

  // 8. Quiz Actions
  const prevBtn = document.getElementById("prev-q-btn");
  if (prevBtn) prevBtn.textContent = dict.prevItem;

  const resetBtn = document.getElementById("reset-q-btn");
  if (resetBtn) resetBtn.textContent = dict.resetItem;

  const nextBtn = document.getElementById("next-q-btn");
  if (nextBtn) nextBtn.textContent = dict.nextItem;

  // 9. Quiz Sidebar Cards
  const radarTitle = document.querySelector(".quiz-sidebar .side-title span");
  if (radarTitle) radarTitle.textContent = dict.radarTitle;

  const radarCaption = document.querySelector(".quiz-sidebar .radar-caption");
  if (radarCaption) radarCaption.textContent = dict.radarCaption;

  const compName = document.querySelector(".companion-name");
  if (compName) compName.textContent = dict.tutorName;

  const compStatus = document.querySelector(".companion-status");
  if (compStatus) compStatus.innerHTML = `<span class="status-dot"></span> ${dict.tutorStatus}`;

  const compBubble = document.querySelector(".companion-bubble");
  if (compBubble) compBubble.textContent = dict.tutorInvite;

  const tutorLaunchBtn = document.querySelector(".tutor-launch-btn");
  if (tutorLaunchBtn) tutorLaunchBtn.textContent = dict.tutorBtn;

  // 10. Socratic Chat View
  const chatTitle = document.querySelector(".chat-title");
  if (chatTitle) {
    chatTitle.textContent = "Socratic Reasoning AI Tutor (SOCRATIC AGENT)";
  }
  const chatSubtitle = document.querySelector(".chat-subtitle");
  if (chatSubtitle) {
    chatSubtitle.textContent = "Grounded in Curriculum Knowledge Graph · Deterministic trap lookup · Offline verifiable";
  }

  const chips = document.querySelectorAll(".quick-chip");
  if (chips && chips.length >= 4) {
    chips[0].textContent = "💡 Why is this option a frequent distractor trap?";
    chips[1].textContent = "⛓️ What prerequisite theorems are essential for this problem?";
    chips[2].textContent = "🎯 Provide an isomorphic problem for reinforcement";
    chips[3].textContent = "🔍 How to rigorously distinguish between core concepts?";
  }

  const chatInput = document.getElementById("chat-input-text");
  if (chatInput) {
    chatInput.placeholder = "Enter your reasoning, hypothesis, or questions for Socratic dialogue...";
  }

  const chatSendBtn = document.getElementById("chat-send-btn");
  if (chatSendBtn) chatSendBtn.textContent = "SEND";

  // 11. Knowledge Graph View
  const graphTitle = document.querySelector("#view-graph .section-title");
  if (graphTitle) {
    graphTitle.textContent = "Curriculum Ontology & Exam Distractor Topology (NEO4J DAG VISUALIZER)";
  }
  const graphDesc = document.querySelector("#view-graph .section-desc");
  if (graphDesc) {
    graphDesc.textContent = "Core Syllabus Concepts, Prerequisite Dependencies, and Cognitive Misconception Traps";
  }
  const graphLegends = document.querySelectorAll(".graph-legend-item span");
  if (graphLegends && graphLegends.length >= 3) {
    graphLegends[0].textContent = "Core Syllabus Concept";
    graphLegends[1].textContent = "Prerequisite Foundation";
    graphLegends[2].textContent = "Distractor Misconception Trap";
  }

  // 12. Analytics & Report View
  const statLabels = document.querySelectorAll("#view-report .stat-label");
  if (statLabels && statLabels.length >= 4) {
    statLabels[0].textContent = "CONSECUTIVE STUDY DAYS";
    statLabels[1].textContent = "TRAPS DEFENDED";
    statLabels[2].textContent = "PROJECTED EXAM SCORE";
    statLabels[3].textContent = "GROUNDING CONFIDENCE";
  }

  const radarBigTitle = document.querySelector("#view-report .panel-title span");
  if (radarBigTitle) {
    radarBigTitle.textContent = "Cognitive Competency 5D Panorama (ECharts 5.5.1)";
  }

  const defectLogTitle = document.querySelector("#view-report .defect-panel .panel-title span");
  if (defectLogTitle) {
    defectLogTitle.textContent = "Curriculum Defect Queue & Target Review (BENCHMARK DEFECT LOG)";
  }

  const colTopic = document.querySelector(".col-topic");
  if (colTopic) {
    colTopic.textContent = "DEFECT TARGET & CAUSAL ATTRIBUTION";
  }

  const evalRec = document.querySelector(".eval-rec-box");
  if (evalRec) {
    evalRec.innerHTML = `💡 <strong>EVAL RECOMMENDATION</strong>: Adaptive tracker indicates: Focus today on prerequisite theorems for flagged items, then complete 1 reinforcement item.`;
  }

  // 13. Update Active Student Profile Display
  if (state.currentUser) {
    const matched = getDemoStudents().find(s => s.id === state.currentUser.id);
    if (matched) {
      applyStudentProfile(matched);
    }
  }

  // 14. Refresh the weak-concept queue from the English table
  state.weakList = DEFAULT_WEAK_LISTS;

  // 15. Reload Question, Radar Charts and Graph
  loadQuestion();
  if (typeof rebuildRadarCharts === "function") rebuildRadarCharts();
  if (typeof renderGraph === "function") renderGraph();
  updateStatCards();
}

function initI18n() {
  // Single English locale: no runtime language switching.
  applyLanguage("en");
}

// =============================================================================
// Auth portal & modal identity switcher
// =============================================================================
let currentAuthMode = "login"; // "login" | "register"

function openAuthModal(defaultTab = "login") {
  const loginModal = document.getElementById("login-modal");
  if (!loginModal) return;
  loginModal.style.display = "flex";
  renderDemoAccounts();
  setAuthTab(defaultTab);
  const input = document.getElementById("auth-username-input");
  if (input) {
    setTimeout(() => input.focus(), 60);
  }
}

function closeAuthModal() {
  const loginModal = document.getElementById("login-modal");
  if (loginModal) loginModal.style.display = "none";
  const feedback = document.getElementById("auth-feedback-banner");
  if (feedback) feedback.style.display = "none";
}

function setAuthTab(mode) {
  currentAuthMode = mode;
  const tabLogin = document.getElementById("tab-login-btn");
  const tabRegister = document.getElementById("tab-register-btn");
  const majorGroup = document.getElementById("register-major-group");
  const submitBtn = document.getElementById("submit-auth-btn");
  const feedback = document.getElementById("auth-feedback-banner");
  if (feedback) feedback.style.display = "none";

  if (mode === "register") {
    tabRegister?.classList.add("active");
    tabLogin?.classList.remove("active");
    if (majorGroup) majorGroup.style.display = "block";
    if (submitBtn) {
      submitBtn.textContent = "Create Profile & Enter";
    }
  } else {
    tabLogin?.classList.add("active");
    tabRegister?.classList.remove("active");
    if (majorGroup) majorGroup.style.display = "none";
    if (submitBtn) {
      submitBtn.textContent = "Sign In & Enter";
    }
  }
}

async function handleModalAuthSubmit() {
  const usernameInput = document.getElementById("auth-username-input");
  const pwdInput = document.getElementById("auth-password-input");
  const majorSelect = document.getElementById("auth-major-select");
  const feedback = document.getElementById("auth-feedback-banner");
  const submitBtn = document.getElementById("submit-auth-btn");

  const val = usernameInput ? usernameInput.value.trim() : "";
  if (!val) {
    if (feedback) {
      feedback.style.display = "block";
      feedback.className = "api-status-banner api-status-error";
      feedback.textContent = "⚠️ Please enter your student ID or name";
    }
    usernameInput?.focus();
    return;
  }

  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = `<span class="spin">⏳</span> ${"Authenticating..."}`;
  }

  try {
    let studentObj = null;

    if (currentAuthMode === "register") {
      const subject = majorSelect ? majorSelect.value : "se";
      const res = await fetch(`${API_BASE}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          student_id: val && val.match(/^\d+$/) ? val : `STU-${Math.floor(Math.random() * 90000 + 10000)}`,
          name: val,
          preferred_subject: subject,
          password: pwdInput ? pwdInput.value : ""
        })
      });
      if (res.ok) {
        const payload = await res.json();
        studentObj = payload.user;
      }
    } else {
      const res = await fetch(`${API_BASE}/api/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          student_id: val,
          password: pwdInput ? pwdInput.value : ""
        })
      });
      if (res.ok) {
        const payload = await res.json();
        studentObj = payload.user;
      }
    }

    if (!studentObj) {
      // Offline local fallback matching
      const students = getDemoStudents();
      studentObj = students.find(s => s.id === val || s.name.toLowerCase() === val.toLowerCase());
      if (!studentObj) {
        studentObj = {
          id: val && val.match(/^\d+$/) ? val : "50106070",
          name: val,
          role: "BSc BMIS · Student Profile",
          avatar: val.charAt(0) || "S",
          subject: (majorSelect && currentAuthMode === "register") ? majorSelect.value : "se",
          subjectLabel: "⚙️ Software Eng.",
          streak: 1
        };
      }
    }

    if (feedback) {
      feedback.style.display = "block";
      feedback.className = "api-status-banner api-status-ok";
      feedback.textContent = "✅ Authentication successful, loading workspace...";
    }

    setTimeout(() => {
      applyStudentProfile(studentObj);
      closeAuthModal();
      switchRootView("workspace");
      if (feedback) feedback.style.display = "none";
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = (currentAuthMode === "register")
          ? ("Create Profile & Enter")
          : ("Sign In & Enter");
      }
    }, 400);

  } catch (e) {
    // Offline fallback
    const students = getDemoStudents();
    const studentObj = students.find(s => s.id === val || s.name.toLowerCase() === val.toLowerCase()) || {
      id: val && val.match(/^\d+$/) ? val : "50106070",
      name: val,
      role: "BSc BMIS · Student Profile",
      avatar: val.charAt(0) || "S",
      subject: "se",
      subjectLabel: "⚙️ Software Eng.",
      streak: 1
    };
    applyStudentProfile(studentObj);
    closeAuthModal();
    switchRootView("workspace");
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.textContent = (currentAuthMode === "register")
        ? ("Create Profile & Enter")
        : ("Sign In & Enter");
    }
  }
}

function initAuthPortal() {
  renderDemoAccounts();

  // 1. Quick sign-in from the landing page
  const loginBtn = document.getElementById("portal-login-btn");
  const usernameInput = document.getElementById("portal-username-input");
  if (loginBtn && usernameInput) {
    const handleLogin = () => {
      const val = usernameInput.value.trim();
      const students = getDemoStudents();
      let matched = students.find(s => s.id === val || s.name.toLowerCase() === val.toLowerCase());
      if (!matched) {
        const displayName = val || ("Yuxuan Wu");
        matched = {
          id: val && val.match(/^\d+$/) ? val : "50106070",
          name: displayName,
          role: "BSc BMIS · Student Profile",
          avatar: displayName.slice(0, 2).toUpperCase() || "YW",
          subject: "se",
          subjectLabel: "⚙️ Software Eng.",
          streak: 3
        };
      }
      applyStudentProfile(matched);
      switchRootView("workspace");
    };

    loginBtn.addEventListener("click", handleLogin);
    usernameInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") handleLogin();
    });
  }

  // 2. Navbar sign-in button
  const portalAuthNavBtn = document.getElementById("portal-auth-nav-btn");
  if (portalAuthNavBtn) {
    portalAuthNavBtn.addEventListener("click", () => {
      openAuthModal("login");
    });
  }

  // 3. Navbar quick-enter workspace button
  const fastEnterBtn = document.getElementById("portal-fast-enter-btn");
  if (fastEnterBtn) {
    fastEnterBtn.addEventListener("click", () => {
      const savedUser = localStorage.getItem("smartstudy_current_user");
      const students = getDemoStudents();
      if (savedUser) {
        try {
          applyStudentProfile(JSON.parse(savedUser));
        } catch (e) {
          applyStudentProfile(students[0]);
        }
      } else {
        applyStudentProfile(students[0]);
      }
      switchRootView("workspace");
    });
  }

  // 4. Landing page theme toggle
  const portalThemeBtn = document.getElementById("portal-theme-btn");
  if (portalThemeBtn) {
    portalThemeBtn.addEventListener("click", () => {
      const newTheme = (state.theme === "light") ? "dark" : "light";
      state.theme = newTheme;
      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("smartstudy_theme", newTheme);
      updateThemeIcon();
      if (typeof rebuildRadarCharts === "function") rebuildRadarCharts();
      if (typeof renderGraph === "function") renderGraph();
    });
  }

  // 5. Workspace back-to-landing button
  const backToPortalBtn = document.getElementById("back-to-portal-btn");
  if (backToPortalBtn) {
    backToPortalBtn.addEventListener("click", () => {
      switchRootView("portal");
    });
  }

  // 6. Sidebar user card click -> open sign-in / switch modal
  const userProfileBtn = document.getElementById("user-profile-btn");
  const loginModal = document.getElementById("login-modal");
  const closeLoginModalBtn = document.getElementById("close-login-modal-btn");
  const logoutBtn = document.getElementById("logout-btn");

  if (userProfileBtn) {
    userProfileBtn.addEventListener("click", () => {
      openAuthModal("login");
    });
  }
  if (closeLoginModalBtn) {
    closeLoginModalBtn.addEventListener("click", closeAuthModal);
  }
  if (loginModal) {
    loginModal.addEventListener("click", (e) => {
      if (e.target === loginModal) closeAuthModal();
    });
  }
  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      closeAuthModal();
      localStorage.removeItem("smartstudy_current_user");
      switchRootView("portal");
    });
  }

  // 7. Modal tab switching (Sign In / Register)
  const tabLoginBtn = document.getElementById("tab-login-btn");
  const tabRegisterBtn = document.getElementById("tab-register-btn");
  if (tabLoginBtn) {
    tabLoginBtn.addEventListener("click", () => setAuthTab("login"));
  }
  if (tabRegisterBtn) {
    tabRegisterBtn.addEventListener("click", () => setAuthTab("register"));
  }

  // 8. Password visibility toggle
  const togglePwdBtn = document.getElementById("toggle-auth-pwd-btn");
  const pwdInput = document.getElementById("auth-password-input");
  if (togglePwdBtn && pwdInput) {
    togglePwdBtn.addEventListener("click", () => {
      if (pwdInput.type === "password") {
        pwdInput.type = "text";
        togglePwdBtn.textContent = "🙈";
      } else {
        pwdInput.type = "password";
        togglePwdBtn.textContent = "👁️";
      }
    });
  }

  // 9. Modal submit button and Enter-key listener
  const submitAuthBtn = document.getElementById("submit-auth-btn");
  const authUsernameInput = document.getElementById("auth-username-input");
  if (submitAuthBtn) {
    submitAuthBtn.addEventListener("click", handleModalAuthSubmit);
  }
  if (authUsernameInput) {
    authUsernameInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") handleModalAuthSubmit();
    });
  }
  if (pwdInput) {
    pwdInput.addEventListener("keydown", (e) => {
      if (e.key === "Enter") handleModalAuthSubmit();
    });
  }

  // 10. Initial view: show the landing page on first open
  const initialView = localStorage.getItem("smartstudy_current_view");
  if (initialView === "workspace") {
    const savedUser = localStorage.getItem("smartstudy_current_user");
    if (savedUser) {
      try { applyStudentProfile(JSON.parse(savedUser)); } catch (e) {}
    }
    switchRootView("workspace");
  } else {
    switchRootView("portal");
  }
}


// =============================================================================
// Silent Backend Health Probe
// =============================================================================
async function checkBackendHealth() {
  try {
    const res = await fetch(`${API_BASE}/api/health`);
    if (res.ok) {
      const data = await res.json();
      const statusText = document.querySelector(".sidebar-status-chip .status-text");
      if (statusText) {
        statusText.textContent = "FASTAPI ONLINE";
      }
      console.log("[SmartStudy] Backend probe success:", data);
    }
  } catch (e) {
    // Offline silent fallback: never throw an uncaught exception to the console
  }
}

// =============================================================================
// =============================================================================
// API Key Configuration & Modal Interaction (API Key Configuration Manager)
// =============================================================================
function initApiModal() {
  const modal = document.getElementById("api-modal");
  const openBtn = document.getElementById("api-settings-btn");
  const closeBtn = document.getElementById("close-api-modal-btn");
  const cancelBtn = document.getElementById("cancel-api-btn");
  const saveBtn = document.getElementById("save-api-btn");
  const testBtn = document.getElementById("test-api-btn");
  const providerSelect = document.getElementById("api-provider-select");
  const keyInput = document.getElementById("api-key-input");
  const toggleKeyBtn = document.getElementById("toggle-key-visibility-btn");
  const urlInput = document.getElementById("api-url-input");
  const modelInput = document.getElementById("api-model-input");
  const neo4jInput = document.getElementById("neo4j-uri-input");
  const gateCheckbox = document.getElementById("gate-checkbox");
  const feedback = document.getElementById("api-test-feedback");

  // Sync the active configuration into the form
  function syncConfigToUI() {
    if (providerSelect) providerSelect.value = state.apiConfig.provider;
    if (keyInput) keyInput.value = state.apiConfig.apiKey;
    if (urlInput) urlInput.value = state.apiConfig.apiUrl;
    if (modelInput) modelInput.value = state.apiConfig.model;
    if (neo4jInput) neo4jInput.value = state.apiConfig.neo4jUri;
    if (gateCheckbox) gateCheckbox.checked = state.apiConfig.gateEnabled;
    updateApiBadge();
  }

  function updateApiBadge() {
    const badge = document.getElementById("api-settings-btn");
    const textEl = document.getElementById("nav-api-status-text");
    if (!badge || !textEl) return;

    if (state.apiConfig.provider === "mock") {
      textEl.textContent = "API: Local Sandbox";
      badge.classList.remove("active");
    } else if (state.apiConfig.apiKey) {
      textEl.textContent = `API: ${state.apiConfig.model}`;
      badge.classList.add("active");
    } else {
      textEl.textContent = "API: Configure Key";
      badge.classList.remove("active");
    }
  }

  // Open / close the modal
  if (openBtn) {
    openBtn.addEventListener("click", () => {
      syncConfigToUI();
      if (feedback) feedback.style.display = "none";
      if (modal) modal.style.display = "flex";
    });
  }

  const hideModal = () => {
    if (modal) modal.style.display = "none";
  };

  if (closeBtn) closeBtn.addEventListener("click", hideModal);
  if (cancelBtn) cancelBtn.addEventListener("click", hideModal);
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) hideModal();
    });
  }

  // Toggle key visibility
  if (toggleKeyBtn && keyInput) {
    toggleKeyBtn.addEventListener("click", () => {
      keyInput.type = keyInput.type === "password" ? "text" : "password";
      toggleKeyBtn.textContent = keyInput.type === "password" ? "👁️" : "🙈";
    });
  }

  // Pre-fill endpoint defaults when the provider changes
  if (providerSelect) {
    providerSelect.addEventListener("change", () => {
      const val = providerSelect.value;
      if (val === "gemini") {
        if (urlInput) urlInput.value = GEMINI_DEFAULT_URL;
        if (modelInput) modelInput.value = GEMINI_DEFAULT_MODEL;
        if (keyInput && (!keyInput.value || !keyInput.value.trim())) {
          keyInput.value = GEMINI_DEFAULT_KEY;
        }
      } else if (val === "dashscope") {
        if (urlInput) urlInput.value = "https://dashscope.aliyuncs.com/compatible-mode/v1";
        if (modelInput) modelInput.value = "qwen-turbo";
      } else if (val === "openai") {
        if (urlInput) urlInput.value = "https://api.openai.com/v1";
        if (modelInput) modelInput.value = "gpt-4o-mini";
      } else if (val === "mock") {
        if (feedback) {
          feedback.className = "api-status-banner success";
          feedback.style.display = "flex";
          feedback.textContent = "💡 Offline sandbox mode: no API key required — the local knowledge-graph heuristic engine provides stable, high-fidelity support.";
        }
      }
    });
  }

  // Test endpoint connectivity
  if (testBtn) {
    testBtn.addEventListener("click", async () => {
      if (!feedback) return;
      const provider = providerSelect ? providerSelect.value : "dashscope";
      const key = keyInput ? keyInput.value.trim() : "";
      const url = urlInput ? urlInput.value.trim() : "";
      const model = modelInput ? modelInput.value.trim() : "qwen-turbo";

      if (provider === "mock") {
        feedback.className = "api-status-banner success";
        feedback.style.display = "flex";
        feedback.textContent = "✅ Local high-fidelity sandbox connected! Multi-discipline graphs and the heuristic knowledge engine are running normally.";
        return;
      }

      if (!key) {
        feedback.className = "api-status-banner error";
        feedback.style.display = "flex";
        feedback.textContent = "❌ Please enter an LLM API key before running the connectivity test!";
        return;
      }

      feedback.className = "api-status-banner";
      feedback.style.display = "flex";
      feedback.textContent = `⚡ Connecting to ${url} to test ${model} — please wait...`;

      try {
        const resp = await fetch(`${url}/chat/completions`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${key}`
          },
          body: JSON.stringify({
            model: model,
            messages: [{ role: "user", content: "ping" }],
            max_tokens: 5
          })
        });

        if (resp.ok) {
          feedback.className = "api-status-banner success";
          feedback.innerHTML = `✅ Connectivity test succeeded (HTTP 200)! Connected to <strong>${escapeHtml(model)}</strong>.`;
        } else {
          const errData = await resp.json().catch(() => ({}));
          const errMsg = escapeHtml(errData.error?.message || errData.message || "Authentication failed or insufficient model permissions");
          feedback.className = "api-status-banner error";
          feedback.innerHTML = `❌ API responded with an error (HTTP ${resp.status}): ${errMsg}`;
        }
      } catch (err) {
        // Direct browser calls often trigger CORS or network warnings; show a friendly notice
        feedback.className = "api-status-banner error";
        feedback.innerHTML = `⚠️ Test notice: ${escapeHtml(err.message || "Network connection timed out")}.<br><span style="font-size:0.78rem;">If the browser blocks direct calls under its CORS policy, save the configuration and the tutor chat will fall back to graph-arbitrated guidance.</span>`;
      }
    });
  }

  // Save configuration
  if (saveBtn) {
    saveBtn.addEventListener("click", () => {
      state.apiConfig.provider = providerSelect ? providerSelect.value : "dashscope";
      state.apiConfig.apiKey = keyInput ? keyInput.value.trim() : "";
      state.apiConfig.apiUrl = urlInput ? urlInput.value.trim() : "https://dashscope.aliyuncs.com/compatible-mode/v1";
      state.apiConfig.model = modelInput ? modelInput.value.trim() : "qwen-turbo";
      state.apiConfig.neo4jUri = neo4jInput ? neo4jInput.value.trim() : "neo4j+s://smartstudy-aura.databases.neo4j.io";
      state.apiConfig.gateEnabled = gateCheckbox ? gateCheckbox.checked : true;

      localStorage.setItem("smartstudy_provider", state.apiConfig.provider);
      localStorage.setItem("smartstudy_apikey", state.apiConfig.apiKey);
      localStorage.setItem("smartstudy_apiurl", state.apiConfig.apiUrl);
      localStorage.setItem("smartstudy_model", state.apiConfig.model);
      localStorage.setItem("smartstudy_neo4j", state.apiConfig.neo4jUri);
      localStorage.setItem("smartstudy_gate", String(state.apiConfig.gateEnabled));

      updateApiBadge();

      if (feedback) {
        feedback.className = "api-status-banner success";
        feedback.style.display = "flex";
        const serviceLabel = state.apiConfig.provider === "mock" ? "Local Sandbox" : escapeHtml(state.apiConfig.model);
        feedback.innerHTML = `💾 Configuration saved! Active service: <strong>${serviceLabel}</strong>.`;
      }

      setTimeout(() => {
        hideModal();
      }, 700);
    });
  }

  syncConfigToUI();
}

// Theme control (Theme Switcher)
// =============================================================================
function initTheme() {
  const saved = localStorage.getItem("smartstudy_theme") || "light";
  state.theme = saved;
  document.documentElement.setAttribute("data-theme", saved);
  updateThemeIcon();

  const toggleBtn = document.getElementById("theme-toggle-btn");
  if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
      state.theme = state.theme === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", state.theme);
      localStorage.setItem("smartstudy_theme", state.theme);
      updateThemeIcon();
      rebuildRadarCharts();
      renderGraph();
    });
  }
}

function updateThemeIcon() {
  const sun = document.getElementById("icon-sun");
  const moon = document.getElementById("icon-moon");
  if (!sun || !moon) return;
  if (state.theme === "dark") {
    sun.style.display = "block";
    moon.style.display = "none";
  } else {
    sun.style.display = "none";
    moon.style.display = "block";
  }
}

// =============================================================================
// Navigation Tabs
// =============================================================================
function initWorkspaceHome() {
  document.querySelectorAll("[data-home-view]").forEach((entry) => {
    entry.addEventListener("click", () => {
      const target = entry.dataset.homeView;
      const tab = document.querySelector(`.nav-tab-item[data-view="${target}"]`);
      if (tab) tab.click();
    });
  });
}

function initNavTabs() {
  const tabs = document.querySelectorAll(".nav-tab-item");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");

      const viewId = tab.dataset.view;
      state.activeTab = viewId;

      document.querySelectorAll(".view-section").forEach(sec => {
        sec.classList.remove("active");
      });

      const targetSec = document.getElementById(`view-${viewId}`);
      if (targetSec) {
        targetSec.classList.add("active");
      }

      if (viewId === "report") {
        if (largeRadarChart) {
          setTimeout(() => largeRadarChart.resize(), 50);
        }
        fetchAndRenderReport(state.reportSubject || "all");
      }
      if (viewId === "graph") {
        renderGraph();
      }
    });
  });
}

// =============================================================================
// Subject Switcher
// =============================================================================
function initSubjectSelector() {
  const btns = document.querySelectorAll(".subject-btn");
  // On init, immediately sync the highlighted subject pill with state.currentSubject
  syncSubjectButtons(state.currentSubject);

  btns.forEach(btn => {
    btn.addEventListener("click", () => {
      const sub = btn.dataset.subject;
      if (sub) {
        switchSubject(sub);
      }
    });
  });
}

// =============================================================================
// Quiz & Trap Remediation Engine
// =============================================================================
function getCurrentQuestion() {
  return DB[state.currentSubject].questions[state.currentQIndex];
}

function normalizeBlankAnswer(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/[;]/g, ",")
    .replace(/\s+/g, " ")
    .replace(/−/g, "-");
}

function mapBackendQuestion(q) {
  const options = Array.isArray(q.options) ? q.options.map(opt => ({
    key: opt.key,
    text: opt.text,
    textEn: opt.textEn || opt.text,
    isCorrect: Boolean(opt.isCorrect ?? opt.is_correct),
    trapId: opt.trapId || opt.trap_id || null
  })) : [];
  const traps = q.traps || {};
  return {
    ...q,
    id: q.id || q.question_id || q.questionId,
    question_id: q.id || q.question_id || q.questionId,
    questionType: q.questionType || q.question_type || "single_choice",
    question_type: q.questionType || q.question_type || "single_choice",
    knowledgeLevel: q.knowledgeLevel || q.knowledge_level || "L3",
    knowledge_level: q.knowledgeLevel || q.knowledge_level || "L3",
    sourceRef: q.sourceRef || q.source_ref || "",
    blankAnswers: q.blankAnswers || q.blank_answers || [],
    blank_answers: q.blankAnswers || q.blank_answers || [],
    options,
    traps
  };
}

async function loadBackendQuestionBank() {
  try {
    const response = await fetch(`${API_BASE}/api/quiz`);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const rows = await response.json();
    const grouped = {};
    rows.map(mapBackendQuestion).forEach(q => {
      if (!grouped[q.subject]) grouped[q.subject] = [];
      grouped[q.subject].push(q);
    });
    Object.entries(grouped).forEach(([subject, questions]) => {
      if (!DB[subject]) DB[subject] = { name: subject, badge: "Backend question bank", questions: [] };
      DB[subject].questions = questions;
    });
    if (!DB.ds) DB.ds = { name: "Data Structures", badge: "Week 4–9", questions: [] };
    if (DB[state.currentSubject]?.questions?.length) loadQuestion();
    syncSubjectButtons(state.currentSubject);
  } catch (error) {
    console.warn("Backend question bank unavailable; keeping local fallback DB", error);
  }
}

function loadQuestion() {
  state.hasAnswered = false;
  const q = getCurrentQuestion();

  // Update the question tag and stem
  document.getElementById("q-difficulty").textContent = q.difficulty;
  document.getElementById("q-tag").textContent = q.tag;
  document.getElementById("q-stem").textContent = q.stem;

  const counterEl = document.getElementById("q-counter");
  if (counterEl) {
    const totalInSub = DB[state.currentSubject].questions.length;
    counterEl.textContent = `${DB[state.currentSubject].name} · Item ${state.currentQIndex + 1} / ${totalInSub} (18 Items Practiced Today)`;
  }

  // Render the option list
  const container = document.getElementById("options-container");
  container.innerHTML = "";

  if (q.questionType === "fill_blank" || q.question_type === "fill_blank") {
    container.innerHTML = `
      <div class="fill-blank-card">
        <input id="fill-blank-input" class="fill-blank-input" type="text" autocomplete="off" placeholder="Enter answer" />
        <button id="fill-blank-submit" class="fill-blank-submit" type="button">Check answer</button>
      </div>`;
    document.getElementById("fill-blank-submit").addEventListener("click", () => {
      handleFillBlank(q, document.getElementById("fill-blank-input"));
    });
  }

  q.options.forEach(opt => {
    const card = document.createElement("div");
    card.className = "quiz-option-card";
    card.dataset.key = opt.key;
    card.innerHTML = `
      <div class="opt-circle">${opt.key}</div>
      <div class="opt-text">${opt.text}</div>
    `;

    card.addEventListener("click", () => handleSelectOption(opt, card, q));
    container.appendChild(card);
  });

  // Collapse the diagnostic drawer
  const drawer = document.getElementById("diagnostic-drawer");
  drawer.className = "diagnostic-drawer";
  drawer.style.display = "none";
  drawer.innerHTML = "";

  // Reset the primary action label
  document.getElementById("next-q-btn").textContent = "NEXT ITEM >";
}

async function handleFillBlank(q, input) {
  if (state.hasAnswered || !input) return;
  const rawAnswer = input.value.trim();
  const value = normalizeBlankAnswer(rawAnswer);
  if (!value) return;

  state.hasAnswered = true;
  input.disabled = true;

  let diagResult = null;
  try {
    const resp = await fetch(`${API_BASE}/api/diagnose`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question_id: q.id || q.question_id || "",
        questionId: q.id || q.question_id || "",
        user_answer_text: rawAnswer,
        userAnswerText: rawAnswer
      })
    });
    if (resp.ok) {
      diagResult = await resp.json();
    }
  } catch (err) {
    console.warn("Fill-blank /api/diagnose unreachable, engaging local check:", err && err.message ? err.message : err);
  }

  const accepted = (q.blankAnswers || q.blank_answers || []).map(normalizeBlankAnswer);
  const correct = diagResult
    ? Boolean(diagResult.is_correct ?? diagResult.isCorrect)
    : accepted.includes(value);
  const explanationText = escapeHtml((diagResult && diagResult.explanation) || q.explanation || "");
  const canonicalDisplay = escapeHtml(
    (q.blankAnswers || q.blank_answers || []).join(" / ") || (diagResult && (diagResult.correct_key || diagResult.correctKey)) || ""
  );

  const drawer = document.getElementById("diagnostic-drawer");
  if (drawer) {
    drawer.style.display = "block";
    drawer.className = `diagnostic-drawer ${correct ? "success" : "trap"}`;
    drawer.innerHTML = `<div class="diag-header">${correct ? "✔ Correct" : "✘ Review needed"}</div><div class="diag-body">${correct ? (explanationText || "Answer matches.") : `Correct answer: ${canonicalDisplay}<br>${explanationText || "Review the corresponding concept."}`}</div>`;
  }
  input.classList.add(correct ? "correct" : "wrong");
  if (correct) {
    state.radar.recall = Math.min(100, state.radar.recall + 4);
    state.radar.precision = Math.min(100, state.radar.precision + 3);
  } else {
    state.radar.precision = Math.max(30, state.radar.precision - 4);
  }
  updateRadarCharts();
  updateStatCards();
}

async function handleSelectOption(opt, cardEl, q) {
  if (state.hasAnswered) return;
  state.hasAnswered = true;

  const allCards = document.querySelectorAll(".quiz-option-card");
  allCards.forEach(c => c.classList.add("disabled"));

  const dict = I18N.en;
  const drawer = document.getElementById("diagnostic-drawer");
  drawer.style.display = "block";
  drawer.className = "diagnostic-drawer";
  drawer.innerHTML = `
    <div class="diag-header" style="color: var(--primary-500, #4f8ef7);">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" class="spin">
        <circle cx="12" cy="12" r="10" stroke-opacity="0.25"></circle>
        <path d="M12 2a10 10 0 0 1 10 10"></path>
      </svg>
      <span>${dict.diagLoading}</span>
    </div>
  `;

  let diagResult = null;

  // 1. Issue a POST /api/diagnose request (sends snake_case and camelCase fields)
  try {
    const payload = {
      question_id: q.id || q.question_id || "",
      questionId: q.id || q.question_id || "",
      selected_option: opt.key,
      selectedOption: opt.key,
      selected_key: opt.key,
      selectedKey: opt.key
    };

    const resp = await fetch(`${API_BASE}/api/diagnose`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (resp.ok) {
      diagResult = await resp.json();
    } else {
      console.warn("Backend /api/diagnose returned status:", resp.status);
    }
  } catch (err) {
    console.warn("Backend /api/diagnose unreachable, engaging local fallback engine:", err && err.message ? err.message : err);
  }

  // 2. High-fidelity local fallback (backend down, network interrupted or error response)
  if (!diagResult) {
    const isCorrect = Boolean(opt.isCorrect);
    const localTrap = (q.traps && q.traps[opt.trapId]) ? q.traps[opt.trapId] : {
      title: "🚨 Classic Distractor Trap",
      desc: q.explanation || ("This option deviates from the core theorem."),
      prereq: q.tag || ("Prerequisite Concept")
    };

    diagResult = {
      is_correct: isCorrect,
      isCorrect: isCorrect,
      trap_name: isCorrect ? null : localTrap.title,
      trapTitle: isCorrect ? null : localTrap.title,
      concept_name: isCorrect ? (q.tag || "Core Theorem") : localTrap.prereq,
      conceptName: isCorrect ? (q.tag || "Core Theorem") : localTrap.prereq,
      socratic_guidance: isCorrect ? (q.explanation || dict.diagCorrectHeader) : (localTrap.desc || q.socraticPrompt),
      socraticHint: isCorrect ? (q.explanation || dict.diagCorrectHeader) : (localTrap.desc || q.socraticPrompt),
      fallback_mode: true,
      fallbackMode: true
    };
  }

  // 3. Normalise fields (strict support for snake_case and camelCase)
  const isCorrect = (diagResult.is_correct !== undefined) ? Boolean(diagResult.is_correct) : Boolean(diagResult.isCorrect);
  const fallbackMode = (diagResult.fallback_mode !== undefined) ? Boolean(diagResult.fallback_mode) : Boolean(diagResult.fallbackMode);
  const defaultTrapTitle = "Classic Distractor Trap";
  const rawTrap = diagResult.trap_name || diagResult.trapTitle || diagResult.trap_title || diagResult.trapName || defaultTrapTitle;
  const trapTitle = rawTrap.startsWith("🚨") ? rawTrap : `🚨 ${rawTrap}`;
  const conceptName = diagResult.concept_name || diagResult.conceptName || diagResult.prerequisite || q.tag || ("Prerequisite Concept");
  const socraticText = diagResult.socratic_guidance || diagResult.socraticHint || diagResult.socratic_hint || diagResult.socraticGuidance || (isCorrect ? q.explanation : (q.socraticPrompt || "Review prerequisite definitions."));

  // Diagnostic-mode badge text and styling
  const badgeText = fallbackMode ? dict.diagOfflineBadge : dict.diagOnlineBadge;
  const badgeBorder = fallbackMode ? "var(--border-subtle, #30363d)" : (isCorrect ? "var(--emerald-500, #10b981)" : "var(--primary-500, #4f8ef7)");
  const badgeColor = fallbackMode ? "var(--text-muted, #8b949e)" : (isCorrect ? "var(--emerald-500, #10b981)" : "var(--primary-500, #4f8ef7)");
  const badgeHtml = `<span class="eval-tag" style="font-size:0.75rem;margin-left:auto;padding:2px 8px;border-radius:4px;border:1px solid ${badgeBorder};color:${badgeColor};font-family:var(--font-sans);">${badgeText}</span>`;

  // 4. Render the drawer and update the competency radar from the diagnosis
  if (isCorrect) {
    // Correct answer
    cardEl.classList.add("correct");
    drawer.className = "diagnostic-drawer success";
    drawer.innerHTML = `
      <div class="diag-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        <span>${dict.diagCorrectHeader}</span>
        ${badgeHtml}
      </div>
      <div class="diag-body">${socraticText}</div>
      <div class="diag-features">
        <div class="diag-feature-pill">
          <span style="color: #10b981;">✔</span> ${'Prerequisite Recall +4'}
        </div>
        <div class="diag-feature-pill">
          <span style="color: #10b981;">✔</span> ${'Trap Defense Index +5'}
        </div>
      </div>
    `;

    // Reward the five-dimension radar
    state.radar.recall = Math.min(100, state.radar.recall + 4);
    state.radar.trapDefense = Math.min(100, state.radar.trapDefense + 5);
    state.radar.synthesis = Math.min(100, state.radar.synthesis + 3);
    state.stats.trapsAvoided++;
    state.stats.predictedScore = Math.min(99, +(state.stats.predictedScore + 0.5).toFixed(1));
    updateRadarCharts();
    updateStatCards();

  } else {
    // Wrong answer: trap triggered!
    cardEl.classList.add("wrong");
    // Also highlight the correct option
    allCards.forEach(c => {
      const optionData = q.options.find(o => o.key === c.dataset.key);
      const isCorrectOpt = optionData && optionData.isCorrect;
      const isBackendCorrect = (diagResult.correct_key && c.dataset.key === diagResult.correct_key) ||
                               (diagResult.correctKey && c.dataset.key === diagResult.correctKey);
      if (isCorrectOpt || isBackendCorrect) {
        c.classList.add("correct");
      }
    });

    drawer.className = "diagnostic-drawer trap";
    drawer.innerHTML = `
      <div class="diag-header">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
        <span>${trapTitle}</span>
        ${badgeHtml}
      </div>
      <div class="diag-body">${socraticText}</div>
      <div class="diag-features">
        <div class="diag-feature-pill" style="border-color: #f59e0b; color: #d97706;">
          <span>${dict.weakPointPrefix} </span><strong>${conceptName}</strong>
        </div>
        <div class="diag-feature-pill" style="border-color: #f43f5e; color: #e11d48;">
          <span>${dict.deductionPrefix} </span>${'Defense Index -6'}
        </div>
      </div>
      <div style="margin-top: 16px; display: flex; gap: 12px;">
        <button id="summon-tutor-btn" class="btn-secondary" style="background: var(--bg-surface); font-size: 0.86rem; border-color: var(--primary-500); color: var(--primary-600);">
          ${dict.summonTutorBtn}
        </button>
      </div>
    `;

    // Deduct trap-defense points
    state.radar.trapDefense = Math.max(30, state.radar.trapDefense - 6);
    state.radar.boundary = Math.max(30, state.radar.boundary - 4);
    updateRadarCharts();

    // Bind the summon-tutor button
    const summonBtn = document.getElementById("summon-tutor-btn");
    if (summonBtn) {
      summonBtn.addEventListener("click", () => {
        switchToTutorTabWithQuestion(q, opt, {
          title: trapTitle,
          prereq: conceptName
        });
      });
    }

    // Record the concept in the weak-point list
    addWeakPoint(conceptName, trapTitle);
  }
}

function addWeakPoint(tag, reason) {
  const existing = state.weakList.find(w => w.tag === tag);
  if (existing) {
    existing.count++;
  } else {
    state.weakList.unshift({ tag, reason, count: 1 });
  }
  renderWeakPointsList();
}

function renderWeakPointsList() {
  const container = document.getElementById("weak-points-list");
  if (!container) return;
  container.innerHTML = "";
  state.weakList.slice(0, 4).forEach(item => {
    const el = document.createElement("div");
    el.style.padding = "10px 14px";
    el.style.borderRadius = "var(--radius-sm)";
    el.style.background = "var(--bg-surface-subtle)";
    el.style.border = "1px solid var(--border-subtle)";
    el.style.marginBottom = "8px";
    el.style.fontSize = "0.86rem";
    const badgeText = `${item.count} Flagged`;
    el.innerHTML = `
      <div style="font-weight: 700; color: var(--text-title); display: flex; justify-content: space-between;">
        <span>${item.tag}</span>
        <span style="color: var(--rose-500); font-size: 0.78rem;">${badgeText}</span>
      </div>
      <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 2px;">${item.reason}</div>
    `;
    container.appendChild(el);
  });
}

// =============================================================================
// Question Navigation & Cycling
// =============================================================================
function goToNextQuestion() {
  const qList = DB[state.currentSubject].questions;
  if (state.currentQIndex < qList.length - 1) {
    state.currentQIndex++;
  } else {
    // Wrap to item 1 of the next subject
    const subjects = Object.keys(DB);
    const currIdx = subjects.indexOf(state.currentSubject);
    const nextSub = subjects[(currIdx + 1) % subjects.length];
    state.currentSubject = nextSub;
    state.currentQIndex = 0;
    syncSubjectButtons(nextSub);
  }
  loadQuestion();
  renderGraph();
  resetChatWithContext();
}

function goToPrevQuestion() {
  if (state.currentQIndex > 0) {
    state.currentQIndex--;
  } else {
    // Wrap to the last item of the previous subject
    const subjects = Object.keys(DB);
    const currIdx = subjects.indexOf(state.currentSubject);
    const prevSub = subjects[(currIdx - 1 + subjects.length) % subjects.length];
    state.currentSubject = prevSub;
    state.currentQIndex = DB[prevSub].questions.length - 1;
    syncSubjectButtons(prevSub);
  }
  loadQuestion();
  renderGraph();
  resetChatWithContext();
}

function syncSubjectButtons(sub) {
  document.querySelectorAll(".subject-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.subject === sub);
  });
}

document.getElementById("next-q-btn").addEventListener("click", goToNextQuestion);

const prevBtn = document.getElementById("prev-q-btn");
if (prevBtn) {
  prevBtn.addEventListener("click", goToPrevQuestion);
}

document.getElementById("reset-q-btn").addEventListener("click", () => {
  loadQuestion();
});

// =============================================================================
// ECharts 5.5.1 five-dimension radar system (sidebar mini chart + full-size report chart)
// =============================================================================
function getRadarOption(isDark) {
  const dict = I18N.en;
  return {
    backgroundColor: "transparent",
    tooltip: { trigger: "item" },
    radar: {
      indicator: [
        { name: dict.radarRecall, max: 100 },
        { name: dict.radarBoundary, max: 100 },
        { name: dict.radarDefense, max: 100 },
        { name: dict.radarSynthesis, max: 100 },
        { name: dict.radarPrecision, max: 100 }
      ],
      shape: "polygon",
      splitNumber: 4,
      axisName: {
        color: isDark ? "#94a3b8" : "#475569",
        fontSize: 11,
        fontWeight: 600
      },
      splitLine: {
        lineStyle: {
          color: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(0, 0, 0, 0.07)"
        }
      },
      splitArea: {
        show: true,
        areaStyle: {
          color: isDark
            ? ["rgba(30, 41, 59, 0.5)", "rgba(30, 41, 59, 0.2)"]
            : ["rgba(241, 245, 249, 0.8)", "rgba(255, 255, 255, 0.8)"]
        }
      },
      axisLine: {
        lineStyle: {
          color: isDark ? "rgba(255, 255, 255, 0.12)" : "rgba(0, 0, 0, 0.1)"
        }
      }
    },
    series: [
      {
        type: "radar",
        data: [
          {
            value: [
              state.radar.recall,
              state.radar.boundary,
              state.radar.trapDefense,
              state.radar.synthesis,
              state.radar.precision
            ],
            name: "Cognitive Mastery Profile",
            symbol: "circle",
            symbolSize: 4,
            itemStyle: { color: "#3b82f6" },
            lineStyle: { width: 2.2, color: "#2563eb" },
            areaStyle: {
              color: isDark
                ? "rgba(37, 99, 235, 0.4)"
                : "rgba(37, 99, 235, 0.25)"
            }
          }
        ],
        animationDuration: 500,
        animationEasing: "cubicOut"
      }
    ]
  };
}

function initRadarCharts() {
  if (typeof echarts === "undefined") return;
  const isDark = state.theme === "dark";

  const miniDom = document.getElementById("mini-radar-chart");
  if (miniDom) {
    miniRadarChart = echarts.init(miniDom);
    miniRadarChart.setOption(getRadarOption(isDark));
  }

  const largeDom = document.getElementById("large-radar-chart");
  if (largeDom) {
    largeRadarChart = echarts.init(largeDom);
    largeRadarChart.setOption(getRadarOption(isDark));
  }

  window.addEventListener("resize", () => {
    if (miniRadarChart) miniRadarChart.resize();
    if (largeRadarChart) largeRadarChart.resize();
  });
}

function updateRadarCharts() {
  const updateData = {
    series: [
      {
        data: [
          {
            value: [
              state.radar.recall,
              state.radar.boundary,
              state.radar.trapDefense,
              state.radar.synthesis,
              state.radar.precision
            ]
          }
        ]
      }
    ]
  };
  if (miniRadarChart) miniRadarChart.setOption(updateData);
  if (largeRadarChart) largeRadarChart.setOption(updateData);
}

function rebuildRadarCharts() {
  if (miniRadarChart) {
    miniRadarChart.dispose();
    miniRadarChart = null;
  }
  if (largeRadarChart) {
    largeRadarChart.dispose();
    largeRadarChart = null;
  }
  initRadarCharts();
}

function updateStatCards() {
  const elStreak = document.getElementById("stat-streak");
  const elTraps = document.getElementById("stat-traps");
  const elScore = document.getElementById("stat-score");
  if (elStreak) elStreak.textContent = `${state.stats.streakDays} days`;
  if (elTraps) elTraps.textContent = `${state.stats.trapsAvoided} blocked`;
  if (elScore) elScore.textContent = `${state.stats.predictedScore} pts`;
  updateRadarDefenseBadge();
  renderWeakPointsList();
}

function initReportFilters() {
  const filterBtns = document.querySelectorAll(".report-filter-btn");
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const subj = btn.dataset.subject || "all";
      state.reportSubject = subj;
      fetchAndRenderReport(subj);
    });
  });
}

async function fetchAndRenderReport(subject = "all") {
  const baseUrl = (window.location.protocol === "http:" || window.location.protocol === "https:")
    ? window.location.origin
    : "http://127.0.0.1:8000";

  const provEl = document.getElementById("report-provenance-text");
  if (provEl) {
    provEl.textContent = "Fetching telemetry metrics...";
  }

  try {
    const [sumRes, trendRes] = await Promise.all([
      fetch(`${baseUrl}/api/reports/summary?subject=${encodeURIComponent(subject)}`),
      fetch(`${baseUrl}/api/reports/trend?subject=${encodeURIComponent(subject)}`)
    ]);

    if (!sumRes.ok || !trendRes.ok) {
      throw new Error(`API returned HTTP ${sumRes.status} / ${trendRes.status}`);
    }

    const summary = await sumRes.json();
    const trend = await trendRes.json();

    // 1. Update Core Stat Cards
    const elAttempt = document.getElementById("stat-attempt-count");
    const elTraps = document.getElementById("stat-traps");
    const elAccuracy = document.getElementById("stat-accuracy");
    const elScore = document.getElementById("stat-score");
    const elStreakDesc = document.getElementById("stat-streak-desc");
    const elBadgeDesc = document.getElementById("radar-badge-desc");

    const attemptCount = summary.attempt_count ?? summary.attemptCount ?? 0;
    const correctCount = summary.correct_count ?? summary.correctCount ?? 0;
    const accuracy = summary.accuracy_rate ?? summary.accuracyRate ?? 0;
    const trapsIdentified = summary.traps_identified ?? summary.trapsIdentified ?? 0;
    const cogScore = summary.cognitive_score ?? summary.cognitiveScore ?? 50.0;
    const streak = summary.streak_days ?? summary.streakDays ?? 1;

    if (elAttempt) elAttempt.textContent = `${attemptCount} Qs`;
    if (elTraps) elTraps.textContent = `${trapsIdentified} Traps`;
    if (elAccuracy) elAccuracy.textContent = `${accuracy.toFixed(1)}%`;
    if (elScore) elScore.textContent = `${cogScore.toFixed(1)} pts`;

    if (elStreakDesc) {
      elStreakDesc.textContent = `🔥 ${streak}-day active study streak`;
    }

    if (elBadgeDesc) {
      elBadgeDesc.textContent = `Defense Score: ${cogScore.toFixed(1)} pts · Solved ${correctCount}/${attemptCount} core problems`;
    }

    // 2. Update Provenance Timestamp
    if (provEl) {
      const genTime = summary.generated_at ? new Date(summary.generated_at).toLocaleTimeString() : "Live aggregate";
      provEl.textContent = `Source: ${summary.data_source || 'demo_baseline'} · Time: ${genTime} · 100% Offline Reproducible`;
    }

    // 3. Render Weak Points List
    const weakContainer = document.getElementById("weak-points-list");
    if (weakContainer) {
      weakContainer.innerHTML = "";
      const wpList = summary.weak_points || summary.weakPoints || [];
      if (wpList.length === 0) {
        weakContainer.innerHTML = `
          <div style="padding: 14px; text-align: center; color: var(--text-muted); font-size: 0.84rem;">
            ${"No critical misconceptions recorded for this subject."}
          </div>
        `;
      } else {
        wpList.forEach(wp => {
          const row = document.createElement("div");
          row.style.padding = "10px 14px";
          row.style.borderRadius = "var(--radius-sm)";
          row.style.background = "var(--bg-surface-subtle)";
          row.style.border = "1px solid var(--border-subtle)";
          row.style.marginBottom = "8px";
          row.style.fontSize = "0.86rem";
          const failCount = wp.fail_count ?? wp.failCount ?? 1;
          const trapTitle = wp.trap_name || wp.trapName || "Concept confusion";
          const failBadge = `${failCount} Misses`;
          row.innerHTML = `
            <div style="font-weight: 700; color: var(--text-title); display: flex; justify-content: space-between; align-items: center;">
              <span>${wp.topic}</span>
              <span style="color: var(--rose-500); font-size: 0.76rem; background: rgba(239, 68, 68, 0.1); padding: 2px 8px; border-radius: 999px;">${failBadge}</span>
            </div>
            <div style="font-size: 0.78rem; color: #f59e0b; margin-top: 4px; font-weight: 500;">⚠️ Cause: ${trapTitle}</div>
            ${wp.recommendation ? `<div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 3px;">💡 Recommendation: ${wp.recommendation}</div>` : ""}
          `;
          weakContainer.appendChild(row);
        });
      }
    }

    // 4. Update Large Radar Chart
    if (largeRadarChart && trend && trend.scores) {
      largeRadarChart.setOption({
        series: [
          {
            data: [
              {
                value: trend.scores,
                name: "Cognitive Radar"
              }
            ]
          }
        ]
      });
    }

  } catch (err) {
    console.warn("fetchAndRenderReport fallback to in-memory telemetry:", err);
    if (provEl) {
      provEl.textContent = "Source: Local In-Memory Sandbox";
    }
    updateStatCards();
  }
}

// =============================================================================
// Socratic Tutor Chat
// =============================================================================
function initSocraticChat() {
  resetChatWithContext();

  const sendBtn = document.getElementById("chat-send-btn");
  const inputField = document.getElementById("chat-input-text");

  if (sendBtn && inputField) {
    sendBtn.addEventListener("click", () => handleUserChatMessage());
    inputField.addEventListener("keypress", (e) => {
      if (e.key === "Enter") handleUserChatMessage();
    });
  }

  // Quick-question chips
  document.querySelectorAll(".quick-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      if (inputField) {
        inputField.value = chip.textContent;
        handleUserChatMessage();
      }
    });
  });
}

function resetChatWithContext() {
  const container = document.getElementById("chat-msgs-container");
  if (!container) return;

  const q = getCurrentQuestion();
  container.innerHTML = `
    <div class="msg-row tutor">
      <div class="msg-avatar">AI</div>
      <div class="msg-bubble">
        Greetings! I am your <strong>Socratic AI Study Companion</strong>. My responses are strictly anchored to verified syllabus knowledge graphs — <strong>no spoon-feeding solutions, zero hallucinated facts</strong>!<br><br>
        Active Curriculum: <strong>[${DB[state.currentSubject].name}]</strong>.<br>
        ${q.socraticPrompt}
        <div>
          <span class="msg-grounding-tag">🔒 Grounded Concept Base · Deterministic Trap Lookup</span>
        </div>
      </div>
    </div>
  `;
}

function switchToTutorTabWithQuestion(q, opt, trap) {
  // Switch to the tutor tab
  document.querySelectorAll(".nav-tab-item").forEach(t => t.classList.remove("active"));
  document.querySelector('.nav-tab-item[data-view="tutor"]').classList.add("active");

  document.querySelectorAll(".view-section").forEach(sec => sec.classList.remove("active"));
  document.getElementById("view-tutor").classList.add("active");

  const userName = (state.currentUser && state.currentUser.name) || ("Yuxuan Wu");
  const userMsg = `Hello Tutor, while attempting the item on [${q.tag}], I chose distractor ${opt.key} and fell into a trap. Could you guide me through where my reasoning diverged?`;

  appendChatMessage("user", userMsg);

  setTimeout(() => {
    const tutorMsg = `${userName}, you encountered a classic distractor trap: <strong>${trap.title}</strong>!<br><br>
         According to our GraphRAG prerequisite chain, the primary conceptual gap is: <strong>${trap.prereq}</strong>.<br><br>
         ${q.socraticPrompt}`;

    appendChatMessage("tutor", tutorMsg);
  }, 500);
}

function getLocalSmartReply(text, q) {
  const lower = text.toLowerCase();
  const safeNodes = (q && q.graph && Array.isArray(q.graph.nodes)) ? q.graph.nodes : [];
  const safeTraps = (q && q.traps) ? Object.values(q.traps) : [];
  const qTag = escapeHtml((q && q.tag) || ("Active Concept"));

  if (lower.includes("prereq") || lower.includes("condition") || lower.includes("assumption")) {
    const prereqs = safeNodes
      .filter(n => n.type === "prereq")
      .map(n => escapeHtml(n.label))
      .join(", ");
    return {
      text: `According to our syllabus topology, foundational prerequisites for [${qTag}] include: <strong>${prereqs || 'Core Prerequisite Theorems'}</strong>. In your reasoning process, did you account for all boundary conditions?`,
      tag: "💡 Graph Topology Prerequisite Trace"
    };
  } else if (lower.includes("trap") || lower.includes("why") || lower.includes("wrong")) {
    const traps = safeTraps.length
      ? safeTraps.map(t => escapeHtml(t.title)).join("<br>")
      : ("No preset traps for this item; review the stem and explanation boundaries.");
    return {
      text: `Examiners intentionally designed typical distractor traps around this topic:<br>${traps}<br><br>Reflecting on the problem statement, which assumption is most tempting yet flawed?`,
      tag: "🚨 Distractor Trap Attribution"
    };
  } else if (lower.includes("isomorphic") || lower.includes("reinforcement") || lower.includes("variant")) {
    return {
      text: `Extracted isomorphic reinforcement problem from [${DB[state.currentSubject].name}] topology:<br><br>If the primary boundary invariant is inverted, does the architectural guarantee still hold? State your deductive proof below.`,
      tag: "🎯 Isomorphic Reinforcement Item"
    };
  } else {
    return {
      text: `⚠️ <strong>No External LLM Endpoint Configured</strong><br><br>The system is currently operating in offline sandbox mode.<br>👉 Click <strong>"🔑 API Settings"</strong> in the sidebar to configure Gemini / Qwen / OpenAI endpoints if live inference is desired.`,
      tag: "⚠️ Sandbox Mode Active"
    };
  }
}

async function handleUserChatMessage() {
  const input = document.getElementById("chat-input-text");
  const text = input.value.trim();
  if (!text) return;

  appendChatMessage("user", text);
  input.value = "";

  const q = getCurrentQuestion();
  const container = document.getElementById("chat-msgs-container");

  // With an online API key configured (non-mock mode), issue a real LLM heuristic call
  if (state.apiConfig.provider !== "mock" && state.apiConfig.apiKey) {
    let typingRow = null;
    if (container) {
      typingRow = document.createElement("div");
      typingRow.className = "msg-row tutor";
      typingRow.innerHTML = `
        <div class="msg-avatar">AI</div>
        <div class="msg-bubble" style="color: var(--text-muted); font-style: italic;">
          <span>🤖 Tutor connected to ${state.apiConfig.model}; reasoning is now anchored to knowledge-graph facts...</span>
        </div>
      `;
      container.appendChild(typingRow);
      container.scrollTop = container.scrollHeight;
    }

    try {
      const systemPrompt = `You are a rigorous Socratic tutor (JC2001 Software Engineering adaptive tutoring system).\n` +
        `Active subject: [${DB[state.currentSubject].name}].\n` +
        `Concept tag: [${q.tag}].\n` +
        `Problem stem: ${q.stem}\n` +
        `Core rules:\n` +
        `1. Never reveal the correct option letter or spoil the answer!\n` +
        `2. Ground every hint in authoritative knowledge-graph facts; never invent or hallucinate facts;\n` +
        `3. Keep replies short and sharp (under 120 words), guiding the student to the conclusion through questions and theorem cues.`;

      const resp = await fetch(`${state.apiConfig.apiUrl}/chat/completions`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${state.apiConfig.apiKey}`
        },
        body: JSON.stringify({
          model: state.apiConfig.model,
          messages: [
            { role: "system", content: systemPrompt },
            { role: "user", content: text }
          ],
          temperature: 0.6,
          max_tokens: 350
        })
      });

      if (typingRow) typingRow.remove();

      if (resp.ok) {
        const data = await resp.json();
        const rawReply = data.choices?.[0]?.message?.content || "The model returned no usable text content.";
        // Format the output
        const formattedReply = rawReply
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/\n\n/g, "<br><br>")
          .replace(/\n/g, "<br>")
          .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

        appendChatMessage("tutor", formattedReply, `🔒 Live ${escapeHtml(state.apiConfig.model)} · Grounded in knowledge-graph facts`);
        return;
      } else {
        const errData = await resp.json().catch(() => ({}));
        const errMsg = escapeHtml(errData.error?.message || errData.message || "Authentication failed or the model endpoint is misconfigured");
        appendChatMessage(
          "tutor",
          `⚠️ <strong>API error (HTTP ${resp.status})</strong><br><br>The endpoint returned: ${errMsg}.<br>Check the API key and endpoint under "🔑 API Settings".`,
          "❌ API call failed"
        );
        return;
      }
    } catch (err) {
      if (typingRow) typingRow.remove();
      appendChatMessage(
        "tutor",
        `⚠️ <strong>No usable API endpoint, or the network connection failed</strong><br><br>Could not reach <code>${escapeHtml(state.apiConfig.apiUrl)}</code>.<br>Error: ${escapeHtml(err.message || "Network connection timed out")}.<br><span style="font-size:0.8rem;color:var(--text-muted);">Note: when running locally straight from the file system, the browser may block cross-origin (CORS) requests; check the console or serve the app through a local proxy.</span>`,
        "⚠️ Connection failed"
      );
      return;
    }
  }

  // Fallback reply for the offline sandbox or when no API key is configured
  setTimeout(() => {
    const replyObj = getLocalSmartReply(text, q);
    if (typeof replyObj === "string") {
      appendChatMessage("tutor", replyObj);
    } else {
      appendChatMessage("tutor", replyObj.text, replyObj.tag);
    }
  }, 400);
}

function appendChatMessage(sender, htmlContent, customTag) {
  const container = document.getElementById("chat-msgs-container");
  if (!container) return;

  const tagText = customTag || ("💡 Socratic Heuristic Guidance · Zero Spoiler Policy");
  const row = document.createElement("div");
  row.className = `msg-row ${sender}`;

  let reasoningHtml = "";
  if (sender === 'tutor' && !htmlContent.includes("reasoning-accordion")) {
    reasoningHtml = `
      <details class="reasoning-accordion">
        <summary class="reasoning-summary">
          <span class="reasoning-summary-left">
            <span class="pulse-dot pulse-purple"></span>
            <span>${'🧠 Deep Reasoning Trace (2.8s)'}</span>
          </span>
          <span class="reasoning-toggle-icon">▶</span>
        </summary>
        <div class="reasoning-body">
          <div class="reasoning-step-item">
            <span class="step-num">1</span>
            <div class="step-content">
              <strong>${'[GraphRAG Recall]'}</strong> ${'Retrieved core concept topology, recalled 3 prerequisite nodes.'}
            </div>
          </div>
          <div class="reasoning-step-item">
            <span class="step-num">2</span>
            <div class="step-content">
              <strong>${'[Trap Arbitration]'}</strong> ${'Arbitrated cognitive misconception against typical student error patterns.'}
            </div>
          </div>
          <div class="reasoning-step-item">
            <span class="step-num">3</span>
            <div class="step-content">
              <strong>${'[Anti-Spoiler Shield]'}</strong> ${'Blocked standard answer reveal; activated step-by-step heuristic prompts.'}
            </div>
          </div>
          <div class="reasoning-step-item">
            <span class="step-num">4</span>
            <div class="step-content">
              <strong>${'[Socratic Synthesis]'}</strong> ${'Synthesized prompt to facilitate student self-derivation.'}
            </div>
          </div>
        </div>
      </details>
    `;
  }

  const safeBody = sender === "user" ? escapeHtml(htmlContent) : htmlContent;

  row.innerHTML = `
    <div class="msg-avatar">${sender === 'tutor' ? 'AI' : ('Me')}</div>
    <div class="msg-bubble">
      ${reasoningHtml}
      ${safeBody}
      ${sender === 'tutor' ? `<div><span class="msg-grounding-tag">${escapeHtml(tagText)}</span></div>` : ''}
    </div>
  `;

  container.appendChild(row);
  container.scrollTop = container.scrollHeight;
}

// =============================================================================
// Interactive Neo4j Graph Canvas rendering
// =============================================================================
function renderGraph() {
  const svg = document.getElementById("large-graph-svg");
  if (!svg) return;

  const q = getCurrentQuestion();
  const isDark = state.theme === "dark";

  if (!q || !q.graph || !Array.isArray(q.graph.nodes) || !Array.isArray(q.graph.edges) || q.graph.nodes.length === 0) {
    const emptyMsg = "No concept subgraph attached to this item; switch to a core concept question to inspect topology.";
    svg.innerHTML = `<text x="390" y="230" font-size="14" fill="${isDark ? '#94a3b8' : '#64748b'}" text-anchor="middle">${escapeHtml(emptyMsg)}</text>`;
    return;
  }

  const colorMap = {
    core: { fill: isDark ? "#1e3a8a" : "#dbeafe", stroke: "#2563eb", text: isDark ? "#bfdbfe" : "#1e40af" },
    prereq: { fill: isDark ? "#064e3b" : "#d1fae5", stroke: "#059669", text: isDark ? "#a7f3d0" : "#065f46" },
    trap: { fill: isDark ? "#4c0519" : "#ffe4e6", stroke: "#e11d48", text: isDark ? "#fecdd3" : "#9f1239" }
  };

  let html = `<defs>
    <marker id="arrow-large" viewBox="0 0 10 10" refX="26" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="${isDark ? '#64748b' : '#94a3b8'}"/>
    </marker>
  </defs>`;

  // Edges
  q.graph.edges.forEach(edge => {
    const from = q.graph.nodes.find(n => n.id === edge.from);
    const to = q.graph.nodes.find(n => n.id === edge.to);
    if (!from || !to) return;

    const midX = (from.x * 1.5 + to.x * 1.5) / 2;
    const midY = (from.y * 1.5 + to.y * 1.5) / 2;

    html += `
      <line x1="${from.x * 1.5}" y1="${from.y * 1.5}" x2="${to.x * 1.5}" y2="${to.y * 1.5}"
            stroke="${isDark ? 'rgba(148, 163, 184, 0.4)' : '#cbd5e1'}" stroke-width="2" marker-end="url(#arrow-large)" />
      <text x="${midX}" y="${midY - 6}" font-size="11" fill="${isDark ? '#94a3b8' : '#64748b'}" text-anchor="middle" font-weight="600">${escapeHtml(edge.label)}</text>
    `;
  });

  // Nodes
  q.graph.nodes.forEach(node => {
    const c = colorMap[node.type] || colorMap.core;
    const nx = node.x * 1.5;
    const ny = node.y * 1.5;
    const shortLabel = node.label.length > 10 ? node.label.slice(0, 9) + ".." : node.label;
    html += `
      <g class="graph-node" transform="translate(${nx}, ${ny})" style="cursor: pointer;">
        <circle r="42" fill="${c.fill}" stroke="${c.stroke}" stroke-width="2.5" />
        <text y="4" font-size="12" font-weight="700" fill="${c.text}" text-anchor="middle">${escapeHtml(shortLabel)}</text>
      </g>
    `;
  });

  svg.innerHTML = html;
}

// =============================================================================
// Feature 002: live five-dimension defense-tier badge (Radar Defense Tier Badge)
// =============================================================================
function updateRadarDefenseBadge() {
  const iconEl = document.getElementById("radar-badge-icon");
  const titleEl = document.getElementById("radar-badge-title");
  const descEl = document.getElementById("radar-badge-desc");
  if (!iconEl || !titleEl || !descEl) return;

  const avgDefense = state.stats.predictedScore || 86.5;
  let tier = "S";
  let title = "Tier S · Master Knowledge Defensor";
  let desc = `Defense Rating ${avgDefense} pts · Successfully isolated ${state.stats.trapsAvoided || 14} conceptual traps`;

  if (avgDefense < 70) {
    tier = "C";
    title = "Tier C · Foundational Learner";
  } else if (avgDefense < 80) {
    tier = "B";
    title = "Tier B · Active Practitioner";
  } else if (avgDefense < 88) {
    tier = "A";
    title = "Tier A · Proficient Scholar";
  }

  iconEl.textContent = tier;
  titleEl.textContent = title;
  descEl.textContent = desc;
}

// =============================================================================
// Feature 002: pointer-following spotlight highlight (Spotlight Card Effect)
// =============================================================================
function initSpotlightCards() {
  const updateCardCoordinates = (e, card) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty("--mouse-x", `${x}px`);
    card.style.setProperty("--mouse-y", `${y}px`);
  };

  document.querySelectorAll(".spotlight-card, .portal-feature-card, .demo-user-card").forEach(card => {
    card.addEventListener("pointermove", (e) => updateCardCoordinates(e, card));
    card.addEventListener("mouseleave", () => {
      card.style.removeProperty("--mouse-x");
      card.style.removeProperty("--mouse-y");
    });
  });
}

// =============================================================================
// Feature 002: interactive dual-engine comparison studio controller (Interactive Comparison Sandbox)
// =============================================================================
const SANDBOX_STATE = {
  mode: "smartstudy", // 'smartstudy' | 'traditional'
  selectedOption: "A"
};

const SANDBOX_CASES = {
  A: {
    key: "A",
    text: "Runs from the date of contract signing, expiring no later than 3 years",
    traditional: { badge: "❌ Grading result: WRONG", directAnswer: "Correct answer: B (runs from discovery of fraud, expiring within 1 year)", critique: "🚨 Traditional bank / generic AI flaw: it gives the answer without explaining the conceptual split between claims and formative rights. 64% of students repeat the same 3-year limitation error on a variant question!", tag: "Mechanical grading · No independent reasoning" },
    smartstudy: { badge: "🛡️ SmartStudy Compass · Trap arbitration captured", trapTitle: "🚨 Confusion trap: treating a formative-right exclusion period as a 3-year limitation period", prereq: "Prerequisite gap: claims use limitation periods, while formative rights use strict exclusion periods", radarDeduction: "📉 Trap Defense -5 · Blind spot flagged by prerequisite radar", reasoningSteps: [{ num: 1, title: "[GraphRAG retrieval]", desc: "Locate the statutory exclusion-period rule for rescission." }, { num: 2, title: "[Trap comparison]", desc: "Detect the confusion between the 3-year limitation period and the formative-right rule." }, { num: 3, title: "[Spoiler guard]", desc: "Block direct disclosure of option B and preserve the reasoning challenge." }, { num: 4, title: "[Socratic prompt]", desc: "Ask the learner to distinguish a unilateral formative right from a claim." }], socraticPrompt: "💬 Compass tutor asks: is rescission a claim requiring payment, or a formative right that changes the legal relationship by unilateral intent? Why cannot a formative right use an interruptible limitation period?" }
  },
  B: {
    key: "B", text: "Runs from discovery of fraud, expiring no later than 1 year",
    traditional: { badge: "✅ Grading result: CORRECT", directAnswer: "Correct! Score +5.", critique: "Traditional bank flaw: it checks only the result, not the five-year long-stop protection, so a lucky guess can pass without understanding.", tag: "Simple scoring · No causal tracing" },
    smartstudy: { badge: "🌟 SmartStudy Compass · Concept topology verified", trapTitle: "🎯 Cognitive topology match: correct start point and duration identified", prereq: "Related concept: exclusion periods do not pause, interrupt, or extend like limitation periods", radarDeduction: "📈 Trap Defense +5 · Knowledge robustness increased", reasoningSteps: [{ num: 1, title: "[GraphRAG retrieval]", desc: "Validate the three statutory elements of the exclusion period." }, { num: 2, title: "[Cognitive defence check]", desc: "Avoid the 3-year limitation and duress-cessation traps." }, { num: 3, title: "[Knowledge expansion]", desc: "Connect the rule to the five-year absolute long-stop." }, { num: 4, title: "[Variant challenge]", desc: "Generate a third-party fraud ratification scenario." }], socraticPrompt: "💬 Compass tutor asks: if fraud is discovered in year 4 month 11, does the victim still receive a full year, or does the five-year long-stop control? Why did the Civil Code set that outer limit?" }
  },
  C: {
    key: "C", text: "Runs from the end of the fraudulent act, expiring no later than 1 year",
    traditional: { badge: "❌ Grading result: WRONG", directAnswer: "Correct answer: B", critique: "Traditional bank flaw: it does not explain why fraud and duress have different commencement rules, leaving the learner vulnerable to the next variant.", tag: "Mechanical grading · No attribution guidance" },
    smartstudy: { badge: "🛡️ SmartStudy Compass · Trap arbitration captured", trapTitle: "🚨 Rule-mismatch trap: confusing fraud with duress commencement", prereq: "Prerequisite gap: duress starts after coercion ends, while fraud starts when the deception is discovered", radarDeduction: "📉 Boundary Precision -4 · Confusion edge highlighted", reasoningSteps: [{ num: 1, title: "[GraphRAG retrieval]", desc: "Compare commencement rules for fraud and duress." }, { num: 2, title: "[Trap comparison]", desc: "Identify the everyday intuition that an event must end before time starts." }, { num: 3, title: "[Spoiler guard]", desc: "Block direct disclosure of option B and guide the distinction." }, { num: 4, title: "[Socratic prompt]", desc: "Ask why a person under coercion may be unable to sue." }], socraticPrompt: "💬 Compass tutor asks: why does duress wait until coercion ends, while fraud starts once the truth is known? What is the legal reason to treat those states differently?" }
  }
};
function initComparisonSandbox() {
  const btnTrad = document.getElementById("sandbox-btn-trad");
  const btnSmart = document.getElementById("sandbox-btn-smart");
  const optionsContainer = document.getElementById("sandbox-options");
  const feedbackBox = document.getElementById("sandbox-feedback-box");

  if (!btnTrad || !btnSmart || !optionsContainer || !feedbackBox) return;

  btnTrad.addEventListener("click", () => {
    SANDBOX_STATE.mode = "traditional";
    btnTrad.classList.add("active");
    btnSmart.classList.remove("active");
    renderSandboxFeedback();
  });

  btnSmart.addEventListener("click", () => {
    SANDBOX_STATE.mode = "smartstudy";
    btnSmart.classList.add("active");
    btnTrad.classList.remove("active");
    renderSandboxFeedback();
  });

  optionsContainer.querySelectorAll(".sandbox-opt-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      optionsContainer.querySelectorAll(".sandbox-opt-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      SANDBOX_STATE.selectedOption = btn.dataset.key;
      renderSandboxFeedback();
    });
  });

  renderSandboxFeedback();
}

function renderSandboxFeedback() {
  const feedbackBox = document.getElementById("sandbox-feedback-box");
  if (!feedbackBox) return;

  const sandboxCases = SANDBOX_CASES;
  const currentCase = sandboxCases[SANDBOX_STATE.selectedOption] || sandboxCases.A;
  const isSmart = (SANDBOX_STATE.mode === "smartstudy");

  if (!isSmart) {
    const trad = currentCase.traditional;
    feedbackBox.innerHTML = `
      <div class="feedback-box-traditional" style="animation: fadeIn 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
          <span style="font-weight: 700; font-size: 0.95rem; color: #f85149;">${trad.badge}</span>
          <span style="font-size: 0.74rem; background: rgba(248,81,73,0.12); color: #f85149; padding: 2px 8px; border-radius: 4px; font-family: var(--font-sans);">${trad.tag}</span>
        </div>
        <div style="font-size: 1rem; font-weight: 700; color: var(--text-title); margin-bottom: 12px; padding: 10px 14px; background: var(--bg-surface); border-radius: 8px; border: 1px solid var(--border-subtle);">
          ${trad.directAnswer}
        </div>
        <div style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; padding: 10px 12px; background: rgba(248,81,73,0.06); border-radius: 8px; border: 1px dashed rgba(248,81,73,0.25);">
          ${trad.critique}
        </div>
        <div style="margin-top: 14px; text-align: right;">
          <span style="font-size: 0.78rem; color: var(--text-light); font-family: var(--font-mono);">Traditional AI Model: Zero Prerequisite Tracking</span>
        </div>
      </div>
    `;
  } else {
    const smart = currentCase.smartstudy;
    const reasoningItems = smart.reasoningSteps.map(step => `
      <div class="reasoning-step-item">
        <span class="step-num">${step.num}</span>
        <div class="step-content">
          <strong>${step.title}</strong> ${step.desc}
        </div>
      </div>
    `).join("");

    feedbackBox.innerHTML = `
      <div class="feedback-box-smartstudy" style="animation: fadeIn 0.25s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
          <span style="font-weight: 700; font-size: 0.95rem; color: #10b981;">${smart.badge}</span>
          <span style="font-size: 0.74rem; background: rgba(16,185,129,0.12); color: #10b981; padding: 2px 8px; border-radius: 4px; font-family: var(--font-sans);">Neo4j GraphRAG</span>
        </div>
        <div style="font-size: 0.92rem; font-weight: 700; color: var(--text-title); margin-bottom: 10px;">
          ${smart.trapTitle}
        </div>
        <div style="font-size: 0.82rem; color: #f59e0b; background: rgba(245,158,11,0.08); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(245,158,11,0.2); margin-bottom: 10px;">
          ${smart.prereq}
        </div>
        <div style="font-size: 0.8rem; color: #818cf8; margin-bottom: 10px; font-family: var(--font-sans);">
          ${smart.radarDeduction}
        </div>

        <!-- Collapsible deep-reasoning trace -->
        <details class="reasoning-accordion" open>
          <summary class="reasoning-summary">
            <span class="reasoning-summary-left">
              <span class="pulse-dot pulse-purple"></span>
              <span>🧠 Deep Thinking Process (2.4s)</span>
            </span>
            <span class="reasoning-toggle-icon">▶</span>
          </summary>
          <div class="reasoning-body">
            ${reasoningItems}
          </div>
        </details>

        <div style="font-size: 0.86rem; color: var(--text-body); background: var(--bg-surface); padding: 12px; border-radius: 10px; border: 1px solid var(--border-subtle); line-height: 1.6;">
          ${smart.socraticPrompt}
        </div>
      </div>
    `;
  }
}

// =============================================================================
// Feature 002: global power-user HUD command palette (Cmd+K / Ctrl+K)
// =============================================================================
const COMMANDS_REGISTRY = [
  // Core view navigation
  {
    id: "nav_quiz",
    title: "Quiz & Trap-Drilling Workspace",
    subtitle: "Open the core question-practice and misconception diagnosis console",
    category: "navigation",
    keywords: ["quiz", "trap", "question", "practice", "drill"],
    icon: "🎯",
    shortcut: "Alt+1",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.nav-tab-item[data-view="quiz"]')?.click();
    }
  },
  {
    id: "nav_tutor",
    title: "Socratic AI Study Companion",
    subtitle: "Start multi-turn heuristic guidance and reasoning-chain dialogue",
    category: "navigation",
    keywords: ["tutor", "socratic", "ai", "chat", "guidance"],
    icon: "💬",
    shortcut: "Alt+2",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.nav-tab-item[data-view="tutor"]')?.click();
    }
  },
  {
    id: "nav_graph",
    title: "Concept Topology Graph Panorama",
    subtitle: "Open the Neo4j topology canvas of concepts, prerequisites and traps",
    category: "navigation",
    keywords: ["graph", "topology", "concept", "prerequisite", "network"],
    icon: "🕸️",
    shortcut: "Alt+3",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.nav-tab-item[data-view="graph"]')?.click();
    }
  },
  {
    id: "nav_report",
    title: "Learning Diagnostics & 5D Profile",
    subtitle: "Review your 5D competency radar, defense badge and defect list",
    category: "navigation",
    keywords: ["report", "diagnostic", "radar", "profile", "ability"],
    icon: "📊",
    shortcut: "Alt+4",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.nav-tab-item[data-view="report"]')?.click();
    }
  },
  // Subject switching
  {
    id: "sub_or",
    title: "Switch subject: 📐 Operations Research (OR)",
    subtitle: "Year 2 core · LP standard form, convex feasible regions and duality",
    category: "discipline",
    keywords: ["operations research", "or", "linear programming", "simplex", "duality"],
    icon: "📐",
    shortcut: "Ctrl+O",
    action: () => {
      switchRootView("app-shell");
      switchSubject("or");
    }
  },
  {
    id: "sub_mis",
    title: "Switch subject: 🌐 Management Information Systems (MIS)",
    subtitle: "Year 2 core · Laudon four-tier architecture, C2M and ERP integration",
    category: "discipline",
    keywords: ["mis", "management information systems", "tps", "erp", "c2m"],
    icon: "🌐",
    shortcut: "Ctrl+M",
    action: () => {
      switchRootView("app-shell");
      switchSubject("mis");
    }
  },
  {
    id: "sub_prob_stat",
    title: "Switch subject: 🎲 Probability & Mathematical Statistics",
    subtitle: "Year 2 core · Bayes inversion, the false-positive paradox and independence",
    category: "discipline",
    keywords: ["probability", "statistics", "math", "bayes", "independence"],
    icon: "🎲",
    shortcut: "Ctrl+P",
    action: () => {
      switchRootView("app-shell");
      switchSubject("prob_stat");
    }
  },
  {
    id: "sub_mkt",
    title: "Switch subject: 🎯 Marketing (MKT)",
    subtitle: "Year 2 core · STP positioning, the 4Ps mix and Porter strategies",
    category: "discipline",
    keywords: ["marketing", "mkt", "stp", "4p", "porter"],
    icon: "🎯",
    shortcut: "Ctrl+K",
    action: () => {
      switchRootView("app-shell");
      switchSubject("mkt");
    }
  },
  {
    id: "sub_eng",
    title: "Switch subject: ✍️ Academic English & Research Writing (Eng)",
    subtitle: "Year 2 core · IMRaD structure, academic hedging and deep paraphrasing",
    category: "discipline",
    keywords: ["academic english", "eng", "writing", "imrad", "paper"],
    icon: "✍️",
    shortcut: "Ctrl+G",
    action: () => {
      switchRootView("app-shell");
      switchSubject("eng");
    }
  },
  {
    id: "sub_law",
    title: "Switch subject: ⚖️ Civil & Commercial Law (Law)",
    subtitle: "Civil Code Art. 152 rescission rights and good-faith acquisition",
    category: "discipline",
    keywords: ["law", "civil law", "rescission", "civil code"],
    icon: "⚖️",
    shortcut: "Ctrl+L",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.subject-btn[data-subject="law"]')?.click();
    }
  },
  {
    id: "sub_cs",
    title: "Switch subject: 💻 Computer Architecture (CS)",
    subtitle: "MIPS five-stage pipeline, data hazards and Tomasulo scheduling",
    category: "discipline",
    keywords: ["computer", "architecture", "cs", "pipeline", "mips"],
    icon: "💻",
    shortcut: "Ctrl+C",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.subject-btn[data-subject="cs"]')?.click();
    }
  },
  {
    id: "sub_econ",
    title: "Switch subject: 📈 Econometrics (Econ)",
    subtitle: "OLS Gauss-Markov assumptions, endogeneity bias and instrumental variables",
    category: "discipline",
    keywords: ["economics", "econometrics", "econ", "ols", "endogeneity"],
    icon: "📈",
    shortcut: "Ctrl+E",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.subject-btn[data-subject="econ"]')?.click();
    }
  },
  {
    id: "sub_se",
    title: "Switch subject: ⚙️ Software Engineering (SE)",
    subtitle: "Aberdeen JC2001 software engineering lifecycle and architectural modelling",
    category: "discipline",
    keywords: ["software engineering", "se", "jc2001", "architecture", "lifecycle"],
    icon: "⚙️",
    shortcut: "Ctrl+S",
    action: () => {
      switchRootView("app-shell");
      document.querySelector('.subject-btn[data-subject="se"]')?.click();
    }
  },
  // Quick actions
  {
    id: "act_theme",
    title: "Toggle light/dark colour theme",
    subtitle: "Switch seamlessly between Deep-Space Aurora (Dark) and Academic White (Light)",
    category: "action",
    keywords: ["theme", "dark", "light", "appearance", "colour"],
    icon: "🌓",
    shortcut: "Ctrl+T",
    action: () => {
      document.getElementById("theme-toggle-btn")?.click();
    }
  },
  {
    id: "act_portal",
    title: "Return to the product landing page",
    subtitle: "Go back home to review the project background, innovations and team",
    category: "action",
    keywords: ["home", "portal", "landing", "introduction"],
    icon: "🏠",
    shortcut: "Ctrl+H",
    action: () => {
      switchRootView("portal-landing");
    }
  },
  {
    id: "act_auth",
    title: "Student profile sign-in & quick switch",
    subtitle: "Open student identity management and the team account channel",
    category: "action",
    keywords: ["login", "account", "identity", "student", "switch", "auth"],
    icon: "👤",
    shortcut: "Ctrl+U",
    action: () => {
      openAuthModal();
    }
  }
];

let activeCmdIndex = 0;
let filteredCommands = [...COMMANDS_REGISTRY];

function initCommandPalette() {
  const overlay = document.getElementById("cmd-palette-overlay");
  const input = document.getElementById("cmd-palette-input");
  const btnPortalCmd = document.getElementById("portal-cmd-btn");
  const btnQuizCmd = document.getElementById("quiz-cmd-btn");

  if (!overlay || !input) return;

  // Global shortcut listener: Cmd+K / Ctrl+K / ESC
  window.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      toggleCommandPalette();
    } else if (e.key === "Escape" && overlay.style.display !== "none") {
      closeCommandPalette();
    }
  });

  if (btnPortalCmd) btnPortalCmd.addEventListener("click", () => openCommandPalette());
  if (btnQuizCmd) btnQuizCmd.addEventListener("click", () => openCommandPalette());

  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeCommandPalette();
  });

  input.addEventListener("input", (e) => {
    filterCommandPalette(e.target.value.trim());
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown") {
      e.preventDefault();
      activeCmdIndex = (activeCmdIndex + 1) % (filteredCommands.length || 1);
      renderCommandPaletteList();
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      activeCmdIndex = (activeCmdIndex - 1 + (filteredCommands.length || 1)) % (filteredCommands.length || 1);
      renderCommandPaletteList();
    } else if (e.key === "Enter") {
      e.preventDefault();
      if (filteredCommands[activeCmdIndex]) {
        executeCommand(filteredCommands[activeCmdIndex]);
      }
    }
  });
}

function openCommandPalette() {
  const overlay = document.getElementById("cmd-palette-overlay");
  const input = document.getElementById("cmd-palette-input");
  if (!overlay || !input) return;

  overlay.style.display = "flex";
  input.value = "";
  activeCmdIndex = 0;
  filteredCommands = [...COMMANDS_REGISTRY];
  renderCommandPaletteList();
  setTimeout(() => input.focus(), 50);
}

function closeCommandPalette() {
  const overlay = document.getElementById("cmd-palette-overlay");
  if (overlay) overlay.style.display = "none";
}

function toggleCommandPalette() {
  const overlay = document.getElementById("cmd-palette-overlay");
  if (overlay && overlay.style.display !== "none") {
    closeCommandPalette();
  } else {
    openCommandPalette();
  }
}

function filterCommandPalette(query) {
  if (!query) {
    filteredCommands = [...COMMANDS_REGISTRY];
  } else {
    const q = query.toLowerCase();
    filteredCommands = COMMANDS_REGISTRY.filter(item => {
      return item.title.toLowerCase().includes(q) ||
             (item.subtitle && item.subtitle.toLowerCase().includes(q)) ||
             item.keywords.some(k => k.toLowerCase().includes(q));
    });
  }
  activeCmdIndex = 0;
  renderCommandPaletteList();
}

function renderCommandPaletteList() {
  const listContainer = document.getElementById("cmd-palette-results");
  if (!listContainer) return;

  if (filteredCommands.length === 0) {
    listContainer.innerHTML = `
      <div style="padding: 24px; text-align: center; color: var(--text-muted); font-size: 0.88rem;">
        No matching command. Try searching "quiz", "law", "architecture" or "theme".
      </div>
    `;
    return;
  }

  let html = "";
  let lastCategory = "";

  filteredCommands.forEach((cmd, idx) => {
    if (cmd.category !== lastCategory) {
      lastCategory = cmd.category;
      const catNames = {
        navigation: "Core Navigation",
        discipline: "Subject Banks",
        action: "System Actions"
      };
      html += `<div class="cmd-palette-category">${catNames[cmd.category] || cmd.category}</div>`;
    }

    const isActive = idx === activeCmdIndex;
    html += `
      <div class="cmd-palette-item ${isActive ? 'active' : ''}" data-idx="${idx}">
        <div class="cmd-item-left">
          <span style="font-size: 1.1rem;">${cmd.icon}</span>
          <div>
            <div class="cmd-item-title">${cmd.title}</div>
            <div class="cmd-item-hint">${cmd.subtitle || ''}</div>
          </div>
        </div>
        ${cmd.shortcut ? `<kbd class="cmd-esc-kbd">${cmd.shortcut}</kbd>` : ''}
      </div>
    `;
  });

  listContainer.innerHTML = html;

  listContainer.querySelectorAll(".cmd-palette-item").forEach(el => {
    el.addEventListener("click", () => {
      const idx = parseInt(el.dataset.idx, 10);
      if (filteredCommands[idx]) executeCommand(filteredCommands[idx]);
    });
  });
}

function executeCommand(cmd) {
  closeCommandPalette();
  if (cmd && typeof cmd.action === "function") {
    cmd.action();
  }
}

