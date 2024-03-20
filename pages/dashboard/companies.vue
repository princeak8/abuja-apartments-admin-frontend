<template>
    <div>
        <Table>
            <TableHeader>
                <TableRow>
                    <TableHead>
                        Avatar
                    </TableHead>
                    <TableHead>
                        Name
                    </TableHead>
                    <TableHead>Username</TableHead>
                    <TableHead>
                        Email
                    </TableHead>
                    <TableHead>Phone number</TableHead>
                    <TableHead class="text-right">
                        Action
                    </TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                <TableRow>
                    <TableCell>
                        <Avatar>
                            <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
                            <AvatarFallback>CN</AvatarFallback>
                        </Avatar>
                    </TableCell>
                    <TableCell class="font-medium">
                        Mr Ahmed Danduma
                    </TableCell>
                    <TableCell>abduldanduma</TableCell>
                    <TableCell>abduldanduma@gmail.com</TableCell>
                    <TableCell>+2347689878498</TableCell>
                    <TableCell class="text-right">
                        <div class="flex gap-3 justify-end">
                            <Button class="bg-sky-400">Edit</Button>
                            <Button class=" bg-red-500">Delete</Button>
                        </div>
                    </TableCell>
                </TableRow>
                <TableRow>
                    <TableCell>
                        <Avatar>
                            <AvatarImage src="https://github.com/radix-vue.png" alt="@radix-vue" />
                            <AvatarFallback>CN</AvatarFallback>
                        </Avatar>
                    </TableCell>
                    <TableCell class="font-medium">
                        Mr Ahmed Danduma
                    </TableCell>
                    <TableCell>abduldanduma</TableCell>
                    <TableCell>abduldanduma@gmail.com</TableCell>
                    <TableCell>+2347689878498</TableCell>
                    <TableCell class="text-right">
                        <div class="flex gap-3 justify-end">
                            <Button class="bg-sky-400">Edit</Button>
                            <Button class=" bg-red-500">Delete</Button>
                        </div>
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

import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
definePageMeta({
    layout: 'dashboard'
})
</script>