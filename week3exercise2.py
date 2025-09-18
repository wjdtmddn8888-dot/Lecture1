class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):
    def hello(self):
        print("Hello from D")
        super().hello()

class E(C):
    pass

class F(B, E):
    pass

print("--- Task 2: F's MRO ---")
mro_list = F.mro()
print(mro_list)

# MRO 순서
explanation = """
F.mro() 순서 설명
F 클래스의 메서드 결정 순서: [F -> B -> E -> C -> A -> object]

1.F: 자기 자신부터 탐색을 시작
2.B: F의 첫 번째 부모 클래스인 B를 탐색
3.E: F의 두 번째 부모 클래스인 E를 탐색
4.C: E의 부모 클래스인 C를 탐색
5.A: B와 C의 공통 부모 클래스인 A는 모든 자식 클래스(B, E, C)가 탐색된 후 마지막에 위치함
6.object: 모든 클래스의 최상위 부모 클래스에서 탐색을 마침

이 순서는 C3 선형화 알고리즘에 따라 결정되고 상속받는 모든 클래스를 방문하되 부모 클래스는 항상 자식 클래스보다 나중에 오는 원칙을 따름
"""
print(explanation)


print("\n--- Task 3: MRO Conflict Error ---")
try:
    class X(A): pass
    class Y(A): pass
    class Z(X, Y): pass
    class W(Y, X): pass
    class MROErrorClass(Z, W): pass
except TypeError as e:
    print(e)