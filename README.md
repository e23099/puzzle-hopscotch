# HopScotch Puzzle

A console board game of "Triangular Peg Solitaire".

see: 

* an online version [here](https://www.mathsisfun.com/games/triangle-peg-solitaire/index.html)

## How to play

1. Choose a node to remove at first step
2. Choose a node to "hop over" another nearby node, to eliminate that nearby one
3. Repeat step 2. until no "hop" can be made. You win if there is only one node left.

## Example

### Step 1: Start a new game
```
python3 main.py
```

the console will display:
```
            (A)

         (B)   (C)

      (D)   (E)   (F)

   (G)   (H)   (I)   (J)

(K)   (L)   (M)   (N)   (O)

```

### Step 2: Remove a node
type in `D` to remove the node at location *D*:
```
d
```

the console will display:
```
            (A)

         (B)   (C)

       D    (E)   (F)

   (G)   (H)   (I)   (J)

(K)   (L)   (M)   (N)   (O)
```

### Step 3: Move a node

move node `M` to `D`, by typing them with a seprating space:
```
m d
```

the console will display:
```
            (A)

         (B)   (C)

      (D)   (E)   (F)

   (G)    H    (I)   (J)

(K)   (L)    M    (N)   (O)
```

if the move is invalid, the console will print the previous status.

