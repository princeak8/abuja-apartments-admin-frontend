<template>
    <DialogContent>
        <DialogHeader>
            <DialogTitle>Add Prospect</DialogTitle>
            
            <div class="mt-4">
                <form class=" space-y-6" @submit="onSubmit">
                    <FormField v-slot="{ componentField }" name="username">
                        <FormItem>
                            <FormLabel>Name</FormLabel>
                            <FormControl>
                                <Input type="text" placeholder="name" v-bind="componentField" />
                            </FormControl>
                            
                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <FormField v-slot="{ componentField }" name="username">
                        <FormItem>
                            <FormLabel>Email</FormLabel>
                            <FormControl>
                                <Input type="email" placeholder="email" v-bind="componentField" />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <FormField v-slot="{ componentField }" name="username">
                        <FormItem>
                            <FormLabel>Phone Number</FormLabel>
                            <FormControl>
                                <Input type="text" placeholder="phone number" v-bind="componentField" />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <FormField v-slot="{ componentField }" name="username">
                        <FormItem>
                            <FormLabel>Description</FormLabel>
                            <FormControl>
                                <Input type="text" placeholder="description" v-bind="componentField" />
                            </FormControl>
                            <FormMessage />
                        </FormItem>
                    </FormField>
                    <Button type="submit">
                        Submit
                    </Button>
                </form>
                
            </div>
        </DialogHeader>

        <DialogFooter>
            
        </DialogFooter>
    </DialogContent>
</template>

<script setup>
import {
    DialogContent,
    DialogFooter,
    DialogHeader,
    DialogTitle
} from '@/components/ui/dialog';
import {
    FormControl,
    FormField,
    FormItem,
    FormLabel,
    FormMessage
} from '@/components/ui/form';
import { toTypedSchema } from '@vee-validate/zod';
import { useForm } from 'vee-validate';
import * as z from 'zod';

const formSchema = toTypedSchema(z.object({
    username: z.string().min(2).max(50),
}))

const form = useForm({
    validationSchema: formSchema,
})

const onSubmit = form.handleSubmit((values) => {
    console.log('Form submitted!', values)
})
</script>

<style></style>