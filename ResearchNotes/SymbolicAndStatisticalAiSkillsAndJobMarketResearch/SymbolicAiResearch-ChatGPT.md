[TOC]

## Symbolic AI

Symbolic AI (sometimes called “Good Old-Fashioned AI” or GOFAI) refers to AI methods that rely on explicit, human-readable, *symbols*, *rules*, and *logic* to represent and manipulate knowledge, as opposed to statistical or neural approaches. 

Unlike modern machine learning, which learns patterns from data, symbolic AI explicitly embeds human expertise and reasoning processes into a program. The core of symbolic AI involves representing a problem in a structured way and then using an "inference engine" to apply rules and facts to derive conclusions.

### References

- *Book:* Nils Nilsson, **Artificial Intelligence: A New Synthesis** (broad overview, symbolic + early connectionist).
- *Book:* Eugene Charniak & Drew McDermott, **Introduction to Artificial Intelligence** (classic symbolic AI textbook).
- *Library Hub:* [PyPI Symbolic AI libraries](https://pypi.org/search/?q=symbolic+ai) – collection of symbolic tools in Python.

### Techniques and Methodologies

#### 1. Logic-based techniques

- **Propositional Logic** – representing knowledge with true/false statements and logical connectives.
- **First-Order Predicate Logic (FOL)** – using quantifiers, variables, and predicates to express richer facts.
- **Automated Theorem Proving** – using logical inference rules (resolution, unification) to derive conclusions.
- **Constraint Logic Programming (CLP)** – combining logic programming with constraints (e.g., Prolog with constraint solvers).

##### References for Logic Programming (Prolog-style Unification in Python)

- *Book:* Ivan Bratko, **Prolog Programming for Artificial Intelligence** (gold standard for logic programming).
- *Library:* [kanren](https://github.com/logpy/logpy) (aka logpy, Python’s logic programming library).
- *Tutorial:* [Declarative Programming in Python with Kanren](https://github.com/logpy/logpy) – examples of unification and relations.

#### 2. Rule-based systems

These are a foundational element of symbolic AI, often used in *expert systems*. They rely on a set of "if-then" rules to encode knowledge and decision-making processes.

- **How it Works:** The system's "knowledge base" contains facts and rules provided by human experts. An "inference engine" takes new data (input) and compares it against the rules. If the `if` part of a rule is true, the `then` part is executed. This process, called *chaining*, can be either *forward chaining* (starting with data to find conclusions) or *backward chaining*** (starting with a goal and working backward to see what data is needed).
- **Example:** A medical diagnosis system could use rules like: `IF patient_has_fever AND patient_has_cough THEN consider_flu`. The system would then check for the patient's symptoms and apply the relevant rule to suggest a diagnosis.

- **Glossary**
  - **Production Rules (IF–THEN rules)** – knowledge expressed as condition-action pairs. Used in expert systems like MYCIN.
  - **Forward Chaining** – start from facts, apply rules, derive new facts (data-driven inference).
  - **Backward Chaining** – start from a goal, work backwards to find supporting facts (goal-driven inference).
  - **Rete Algorithm** – efficient pattern-matching for applying large sets of rules.

##### References

- *Book:* Peter Jackson, **Introduction to Expert Systems** (classic treatment of production systems).
- *Tutorial:* [Rule-Based Expert Systems in Python](https://towardsdatascience.com/build-an-expert-system-in-python-a6f032b8e9a9) (Towards Data Science).
- *Library:* [experta](https://github.com/noxdafox/experta) (Python expert system library, based on CLIPS).

#### 3. Search-based symbolic methods

- **State Space Search** – representing problems as states and transitions (used in planning, games).
- **Graph Search Algorithms** – BFS, DFS, A*, AO* applied to symbolic problem representations.
- **Game Tree Search** – minimax, alpha-beta pruning in symbolic representations of games like chess.

##### References

- *Book:* Stuart Russell & Peter Norvig, **Artificial Intelligence: A Modern Approach** (AIMA) — Chapter on Search.
- *Reference Code:* [AIMA Python](https://github.com/aimacode/aima-python) – official Python implementations from the textbook.
- *Tutorial:* [A* Search Algorithm in Python](https://www.redblobgames.com/pathfinding/a-star/introduction.html) – fantastic visual + code explanation.

#### 4. Knowledge representation frameworks

- **Semantic Networks** – graph-like structures with nodes (concepts) and edges (relations).
- **Frames and Scripts** – structured data templates for representing stereotypical situations (e.g., “going to a restaurant”).
- **Ontologies** – hierarchical symbolic knowledge structures (e.g., OWL, Cyc).
- **Conceptual Dependency Theory** – representing natural language meaning in symbolic forms.

##### References

- *Book:* John F. Sowa, **Knowledge Representation: Logical, Philosophical, and Computational Foundations**.
- *Book:* Ronald Brachman & Hector Levesque, **Knowledge Representation and Reasoning**.
- *Tutorial:* [Semantic Networks in AI](https://www.geeksforgeeks.org/semantic-networks-in-artificial-intelligence/) (GeeksforGeeks intro).
- *Library:* [Owlready2](https://owlready2.readthedocs.io/en/latest/) – ontology/semantic web library in Python.



#### 5. Planning and reasoning

- **STRIPS (Stanford Research Institute Problem Solver)** – early planning system with symbolic action schemas.
- **Hierarchical Task Networks (HTN Planning)** – breaking goals into symbolic sub-goals.
- **Temporal Logic for Planning** – symbolic representation of time-dependent actions.

#### 6. Case-based and model-based reasoning

- **Case-Based Reasoning (CBR)** – solve new problems by analogy to stored symbolic cases.
- **Model-Based Reasoning** – use symbolic models of systems (e.g., diagnostic reasoning about circuits).

#### 7. Knowledge engineering methodologies

- **Expert Systems Design** – eliciting expert knowledge into symbolic rules (e.g., MYCIN, DENDRAL).
- **Knowledge Acquisition** – building symbolic knowledge bases from interviews, manuals, or structured input.
- **Meta-reasoning** – reasoning about the reasoning process itself using symbolic representations.

#### 8. Symbolic Natural Language Processing (pre-ML era)

- **Parsing with Grammars (CFG, ATN, DCG)** – symbolic representations of syntax.
- **Semantic Parsing** – mapping sentences into logical forms.
- **Rule-based Machine Translation** – dictionary + grammar driven symbolic translation.

##### References

- *Book:* Daniel Jurafsky & James H. Martin, **Speech and Language Processing** (classic NLP textbook, has symbolic parsing chapters).
- *Library:* [NLTK CFG Documentation](https://www.nltk.org/howto/parse.html) – context-free grammars and parsers in Python.
- *Tutorial:* [Context Free Grammar Parsing with NLTK](https://www.nltk.org/book/ch08.html) (official NLTK book, Chapter 8).



👉 In practice, **Prolog** is the quintessential symbolic AI programming language, while **LISP** pioneered symbolic data structures and rule-based reasoning. Many symbolic AI systems mix these techniques—for example, an expert system might use **rules (if–then)**, **logic inference**, and **frames** together.



### Symbolic AI techniques in Python

Python doesn’t have symbolic AI “built-in” like Prolog or Lisp, but you can implement the same ideas using libraries or custom code.

Here are **examples of major symbolic AI programming techniques in Python**:

#### 1. Rule-Based System (IF–THEN rules, forward chaining)

```
# Simple production-rule system

facts = {"fever", "cough"}

rules = [
    {"if": {"fever", "cough"}, "then": "flu"},
    {"if": {"rash"}, "then": "measles"},
]

inferred = set()

changed = True
while changed:
    changed = False
    for rule in rules:
        if rule["if"].issubset(facts) and rule["then"] not in facts:
            facts.add(rule["then"])
            inferred.add(rule["then"])
            changed = True

print("Inferred facts:", inferred)
# Output: Inferred facts: {'flu'}
```

This is a **forward-chaining expert system** style reasoning.



#### 2. Logic Programming with kanren (Prolog-style unification)

Install: pip install kanren

```
from kanren import run, var, Relation, facts

# Define a relation: parent
parent = Relation()
facts(parent, ("john", "mary"),
              ("mary", "susan"),
              ("john", "alex"))

x = var()
# Query: who are John's children?
children = run(0, x, parent("john", x))
print("John's children:", children)
# Output: John's children: ('mary', 'alex')
```

This mimics **Prolog-style symbolic logic inference**.

#### 3. Search in a Symbolic State Space



Classic **A\*** search for a pathfinding problem.

```
import heapq

def a_star(start, goal, neighbors, heuristic):
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for next_node, cost in neighbors(current):
            new_cost = cost_so_far[current] + cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from[node]
    return path[::-1]

# Example: grid neighbors
def neighbors(node):
    x, y = node
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        yield (x+dx, y+dy), 1

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

print(a_star((0,0), (2,2), neighbors, heuristic))
# Output: [(0,0), (1,0), (2,0), (2,1), (2,2)]
```

That’s a **symbolic search algorithm**.



#### 4. Symbolic Knowledge Representation (Semantic Network)



```
# Very simple semantic network

semantic_net = {
    "bird": {"is_a": "animal", "can": "fly"},
    "penguin": {"is_a": "bird", "can": "swim"},
}

def query(entity, relation):
    if relation in semantic_net.get(entity, {}):
        return semantic_net[entity][relation]
    elif "is_a" in semantic_net.get(entity, {}):
        return query(semantic_net[entity]["is_a"], relation)

print("What can a penguin do?", query("penguin", "can"))
# Output: swim
```

This mimics **inheritance in semantic networks**.



------



#### 5. Natural Language Parsing with CFGs (symbolic NLP)



```
import nltk
from nltk import CFG

grammar = CFG.fromstring("""
  S -> NP VP
  NP -> 'John' | 'Mary'
  VP -> V NP
  V -> 'loves' | 'hates'
""")

parser = nltk.ChartParser(grammar)

for tree in parser.parse(['John', 'loves', 'Mary']):
    print(tree)
    tree.pretty_print()
```

That’s a **rule-based symbolic grammar parser**.



### Which are Still Relevant / Actively Used?

#### 1. Rule-Based Systems (Business Rules Engines)

- **Where used:**
  - Finance (fraud detection, loan approval rules)
  - Healthcare (clinical decision support, diagnostic checks)
  - Enterprise software (insurance claims, eligibility, compliance)
- **Tools/Frameworks:**
  - Drools (Java),
  - Experta (Python),
  - Camunda BPMN with decision tables
- **Why important:**
  - Rules are transparent, auditable, and easy to modify.
  - Widely used in **regulatory/compliance-heavy industries**.

#### 2. Constraint Logic & Constraint Solvers

- **Where used:**
  - Scheduling (airlines, staff rostering, delivery routes)
  - Optimization (supply chain, manufacturing)
  - Configuration (e.g., product option selection in e-commerce or hardware design)
- **Tools:**
  - Google OR-Tools,
  - Z3 Theorem Prover (Microsoft),
  - Choco Solver
- **Why important:**
  - Constraint solving is a **core practical problem** across logistics and operations.

#### 3. Search Algorithms (Symbolic State-Space Search)

- **Where used:**
  - Pathfinding (games, robotics, navigation apps)
  - Puzzle solvers, planners, game AI
  - Automated testing (symbolic execution tools)
- **Tools:**
  - A* in game engines,
  - OR-Tools routing solver,
  - Symbolic execution tools like KLEE
- **Why important:**
  - Every developer working in **games, robotics, or optimization** will likely encounter symbolic search techniques.

#### 4. Knowledge Representation (Ontologies, Semantic Web)

- **Where used:**
  - Enterprise data integration (knowledge graphs, linked data)
  - Healthcare (SNOMED CT, ICD-10, biomedical ontologies)
  - Search engines (Google Knowledge Graph)
- **Tools:**
  - RDF/OWL,
  - Protégé,
  - Owlready2 (Python ontology library)
- **Why important:**
  - Used in **data-rich industries** for reasoning, semantic search, and interoperability.

#### 5. Rule-Based NLP (Symbolic + ML Hybrid Systems)

- **Where used:**
  - Chatbots (pattern-based fallback alongside ML models)
  - Information extraction (regex + rules before/after ML)
  - Legal/medical document processing (symbolic rules to ensure compliance)
- **Tools:**
  - spaCy’s rule-based matcher,
  - NLTK grammars,
  - Hybrid ML+symbolic systems in Rasa, Dialogflow
- **Why important:**
  - Symbolic methods act as **safety nets or precision tools** in NLP pipelines.

### Less Common Today (Mostly Academic/Legacy)

- **Pure Expert Systems (like MYCIN, DENDRAL)** → mostly replaced by ML, though business rules systems are their descendants.
- **Full-blown Prolog-style Logic Programming** → rarely used in mainstream jobs, but still taught for reasoning concepts.
- **STRIPS/HTN Classical Planning** → more academic; in practice, simpler heuristics or ML planning are used.
- **Frames and Scripts (classic KR structures)** → now mostly history, though ideas live on in ontologies and schema.org.

### Bottom Line for Developers

If you’re a software developer today, the symbolic AI methods worth knowing **in practice** are:

1. **Rule-based systems** (business rules, decision tables, compliance logic).
2. **Constraint solving & optimization** (Google OR-Tools, Z3).
3. *Search algorithms (especially A)** (games, robotics, logistics).
4. **Knowledge graphs & ontologies** (enterprise data, semantic web).
5. **Hybrid symbolic NLP** (regex/rules + ML).

The rest (Prolog, STRIPS, semantic networks) are mainly educational: great for understanding AI’s foundations, but less likely to be job-critical.



### Symbolic AI Methods by Job Domain

#### Fintech / Banking / Insurance

- Most relevant symbolic AI:
  1. **Rule-based systems** → fraud detection, eligibility checks, compliance.
  2. **Constraint solvers** → risk modeling, portfolio balancing.
- **Tools you’d encounter:** Drools, Experta (Python), Camunda DMN tables, Z3.
- **Why:** These industries need **auditable, explainable decisions** — perfect for symbolic rules.

#### Healthcare / Biotech

- **Most relevant symbolic AI:**
  1. **Rule-based expert systems** → clinical decision support (e.g., “if fever + rash → measles”).
  2. **Ontologies & knowledge graphs** → SNOMED CT, ICD-10, biomedical vocabularies.
- **Tools:** Owlready2 (Python), Protégé, FHIR standards.
- **Why:** Medical reasoning must be **transparent, standardized, and interoperable**.

#### Logistics / Supply Chain / Manufacturing

- **Most relevant symbolic AI:**
  1. **Constraint solving** → vehicle routing, staff scheduling, warehouse optimization.
  2. *Search (A)** → shortest paths for routing & navigation.
- **Tools:** Google OR-Tools, Choco Solver, OptaPlanner.
- **Why:** These domains are **combinatorial optimization heavy**; symbolic solvers excel here.

#### Game Development

- **Most relevant symbolic AI:**
  1. *Search algorithms (BFS, DFS, A)** → NPC pathfinding.
  2. **Rule-based behavior trees** → enemy AI, decision-making.
- **Tools:** Built-in engines (Unity AI NavMesh, Unreal Behavior Trees).
- **Why:** Games need **fast, deterministic AI** — symbolic methods are lightweight and reliable.

#### Robotics / Autonomous Systems

- **Most relevant symbolic AI:**
  1. **Search + A*** → navigation and motion planning.
  2. **Constraint solving** → task scheduling, multi-robot coordination.
  3. **Hybrid planning (symbolic + probabilistic)** → combining symbolic task reasoning with ML-based perception.
- **Tools:** ROS MoveIt (motion planning), OMPL, Google OR-Tools.
- **Why:** Robots need **deterministic planning** for safety-critical tasks.

#### Web / Enterprise Software

- **Most relevant symbolic AI:**
  1. **Business rules engines** → eligibility, pricing, workflows.
  2. **Knowledge graphs / semantic web** → recommendation, search, data integration.
- **Tools:** Drools, Camunda, RDF/OWL/SPARQL.
- **Why:** Symbolic AI powers **transparent business logic** and **semantic search**.

#### LegalTech / GovTech

- **Most relevant symbolic AI:**
  1. **Rule-based NLP** → extracting structured information from contracts/regulations.
  2. **Ontologies** → modeling legal concepts.
- **Tools:** spaCy rule matcher, NLTK grammars, RDF legal ontologies.
- **Why:** Laws are essentially **symbolic rule systems**; symbolic AI maps naturally here.

####  TL;DR Cheat Sheet

- **Fintech/Insurance →** Rules + Constraint Solvers
- **Healthcare →** Rules + Ontologies
- **Logistics →** Constraint Solvers + Search
- **Games →** Search (A*) + Rules (behavior trees)
- **Robotics →** Search + Constraints + Planning
- **Enterprise →** Rules + Knowledge Graphs
- **Legal/Government →** Rules + Symbolic NLP



---

This document was drafted by Brian Bird using ChatGPT 5 and Gemini 2.5 Flash 8/22/25

---