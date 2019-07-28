fn solve() -> i32 {
    let mut sum = 0;
    for i in 1..1000 {
      if i % 3 == 0 || i % 5 == 0 {
        sum += i;
      }
    }
    sum
}

fn solve2() -> i32 {
    let numbers = (1..1000).filter(|i| i % 3 == 0 || i % 5 == 0);
    numbers.fold(0, |acc, x| acc + x)
}

fn main() {
    println!("Total sum: {}", solve2());
}
