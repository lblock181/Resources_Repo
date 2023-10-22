/// This code snippet is for single and double linked lists
/// To use a single linked list removed the following:
///     Node.prev
///     ListIterator struct & impls

use std::cell::{RefCell};
use std::rc::Rc;

// Need to have the links/nodes be Rc<RefCell>> to provide interior mutability
type Link = Option<Rc<RefCell<Node>>>;

#[derive(Clone)]
struct Node { 
    value: String,
    next: Link,
}

impl Node {
    fn new(val: String) -> Rc<RefCell<Node>> {
        Rc::new(RefCell::new(Node { value: val, next: None }))
    }
}
struct Log {
    head: Link,
    tail: Link,
    pub length: u64,
}

impl Log {
    pub fn new_empty_log() -> Log {
        Log { head: None, tail: None, length: 0 }
    }

    pub fn append(&mut self, val: String) {
        let new_node = Node::new(val);
        match self.tail.take() {
            Some(old_node) => old_node.borrow_mut().next = Some(new_node.clone()),
            None => self.head = Some(new_node.clone())
        };
        self.length += 1;
        self.tail = Some(new_node);
    }

    pub fn pop(&mut self) -> Option<String> {
        self.head.take().map(|head_node| {
            if let Some(next) = head_node.borrow_mut().next.take() {
                self.head = Some(next);
            } else {
                self.tail.take();
            }
            self.length -= 1;
            Rc::try_unwrap(head_node)
                .ok()
                .expect("ERROR: No head node found!!")
                .into_inner()
                .value
        })
    }
}


fn main() {
    println!("Hello, world!");
}
