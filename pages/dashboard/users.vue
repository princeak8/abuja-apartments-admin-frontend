<template>
    <div>
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead>
                        Name
                    </TableHead>
                    <TableHead>Email</TableHead>
                    <TableHead>Phone number</TableHead>
                    <TableHead class="text-right">
                        Action
                    </TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                <TableRow>
                    <TableCell class="font-medium">
                        Mr Ahmed Danduma
                    </TableCell>
                    <TableCell>abduldanduma@gmail.com</TableCell>
                    <TableCell>+2347689878498</TableCell>
                    <TableCell class="text-right">
                        <Button>Edit</Button>
                        <Button>Delete</Button>
                    </TableCell>
                </TableRow>
            </TableBody>
        </Table>
    </div>
</template>

<script setup>
import {
Table,
TableBody,
TableCell,
TableHead,
TableHeader,
TableRow
} from '@/components/ui/table';
definePageMeta({
    layout: 'dashboard'
})
</script>