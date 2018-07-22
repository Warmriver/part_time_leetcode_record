package main

import (
	"fmt"
	"Container/list"
)

type TreeNode struct{
	Val int
	Left *TreeNode
	Right *TreeNode
}


//func inorderTraversal(root *TreeNode) []int{
func inorderTraversal(root *TreeNode) []int{
	nums := list.New()
	if root != nil {
		nums.pushBack(pushToList(root.Left))
		nums.pushBack(root.Val)
		nums.pushBack(pushToList(root.Right))
	}
	return nums;
	//	ret = make([]int, nums.Len())
}

func pushToList(root *TreeNode) list{
	nums := list.New()
	if root != nil {
		nums.pushBack(pushToList(root.Left))
		nums.pushBack(root.Val)
		nums.pushBack(pushToList(root.Right))
	}
	return nums;
}

// moris approach
func moris(root *TreeNode) []int{
	ret := make([]int)
	curr = root
	while curr != nil {
		if curr.Left != nil {
			ret.append(curr.Val)
			curr = curr.Right
		}else{
			pre = curr.Left
			temp = curr
			while pre.Right != nil{
				pre = pe.Right
			}
			pre.Right = curr
			curr = curr.Left
			temp.Left = nil
		}
		return ret 


	} 
}


func main(){
	root := TreeNode{
		
	}
}
