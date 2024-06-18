<template>
    <div>

        <div class="mb-4">
            <h1 class="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white">All Prospects</h1>
        </div>

        <div class="sm:flex mb-4">

            <div>
                <Select>
                    <SelectTrigger class="w-[180px]">
                        <SelectValue placeholder="Select a month" />
                    </SelectTrigger>
                    <SelectContent>
                        <SelectGroup>
                            <SelectLabel>Fruits</SelectLabel>
                            <SelectItem value="apple">
                                Apple
                            </SelectItem>
                            <SelectItem value="banana">
                                Banana
                            </SelectItem>
                            <SelectItem value="blueberry">
                                Blueberry
                            </SelectItem>
                            <SelectItem value="grapes">
                                Grapes
                            </SelectItem>
                            <SelectItem value="pineapple">
                                Pineapple
                            </SelectItem>
                        </SelectGroup>
                    </SelectContent>
                </Select>
            </div>
        </div>
        <div class="sm:flex mb-4">
            <div class="items-center hidden mb-3 sm:flex sm:divide-x sm:divide-gray-100 sm:mb-0 dark:divide-gray-700">
                <form class="lg:pr-3" action="#" method="GET">
                    <label for="users-search" class="sr-only">Search</label>
                    <div class="relative mt-1 lg:w-64 xl:w-96">
                        <input type="text" name="email" id="users-search"
                            class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
                            placeholder="Search for users">
                    </div>
                </form>
            </div>
            <div class="flex items-center ml-auto space-x-2 sm:space-x-3">
                <div class=" text-xl">
                    Engagements <Badge class="mr-4 text-xl">234</Badge>
                    Conversion rate <Badge class="mr-4 text-xl">35%</Badge>
                </div>
                <Button type="button" class="py-2 bg-blue-800">
                    <svg class="w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" width="20" height="20"
                        viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                        stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z">

                        </path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                    <NuxtLink to="/dashboard/send-message">
                        Send bulk message
                    </NuxtLink>
                </Button>
                <Dialog>
                    <DialogTrigger :as="Button" type="button" data-modal-target="add-user-modal"
                        data-modal-toggle="add-user-modal" class="py-2 bg-blue-800">
                        <svg class="w-5 h-5 mr-2 -ml-1" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                                d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                                clip-rule="evenodd"></path>
                        </svg>
                        Add Prospect
                    </DialogTrigger>
                    <AddProspectsModal />
                </Dialog>

                <a href="#"
                    class="inline-flex items-center justify-center w-1/2 px-3 py-2 text-sm font-medium text-center text-gray-900 bg-white border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:ring-primary-300 sm:w-auto dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700">
                    <svg class="w-5 h-5 mr-2 -ml-1" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z"
                            clip-rule="evenodd"></path>
                    </svg>
                    Export
                </a>
            </div>
        </div>
        <Table>
            <thead class="bg-gray-100 dark:bg-gray-700"></thead>
            <TableHeader class="bg-gray-100 dark:bg-gray-700">
                <TableRow>

                    <TableHead>
                        Avatar
                    </TableHead>
                    <TableHead>
                        Name
                    </TableHead>

                    <TableHead>
                        Description
                    </TableHead>
                    <TableHead>Phone number</TableHead>
                    <TableHead>
                        Added at
                    </TableHead>
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
                        <div class="text-base font-semibold text-gray-900 dark:text-white">Mr Ahmed Danduma</div>
                        <div class="text-sm font-normal text-gray-500 dark:text-gray-400">abduldanduma@gmail.com</div>
                    </TableCell>

                    <TableCell>thsis allshds asksalas </TableCell>
                    <TableCell>+2347689878498</TableCell>
                    <TableCell>20th Jan, 2024 | 4:00 pm</TableCell>
                    <TableCell class="text-right">
                        <div class="flex gap-3 justify-end">


                            <Button class="bg-blue-800 text-xs" type="button" @click="onSendMessagePress">
                                <svg class="w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path
                                        d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z">

                                    </path>
                                    <polyline points="22,6 12,13 2,6"></polyline>
                                </svg>
                                Send message
                            </Button>

                            <Button class=" bg-green-900 text-xs" type="button" @click="openRegisterCall">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" class="feather feather-phone mr-2">
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z">
                                    </path>
                                </svg>

                                Register Call
                            </Button>
                            <Button class=" bg-green-500 text-xs" type="button" @click="openSchedule">

                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" class="feather feather-bell mr-2">
                                    <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                                    <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                                </svg>

                                Schedule Meeting
                            </Button>

                            <Button class="bg-blue-800 text-xs">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z">
                                    </path>
                                    <path fill-rule="evenodd"
                                        d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </Button>
                            <Button class="bg-red-500">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                                        clip-rule="evenodd"></path>
                                </svg>

                            </Button>
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
                        <div class="text-base font-semibold text-gray-900 dark:text-white">Mr Ahmed Danduma</div>
                        <div class="text-sm font-normal text-gray-500 dark:text-gray-400">abduldanduma@gmail.com</div>
                    </TableCell>

                    <TableCell>thsis allshds asksalas </TableCell>
                    <TableCell>+2347689878498</TableCell>
                    <TableCell>20th Jan, 2024 | 4:00 pm</TableCell>
                    <TableCell class="text-right">
                        <div class="flex gap-3 justify-end">


                            <Button class="bg-blue-800 text-xs" type="button" @click="onSendMessagePress">
                                <svg class="w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                    viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path
                                        d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z">

                                    </path>
                                    <polyline points="22,6 12,13 2,6"></polyline>
                                </svg>
                                Send message
                            </Button>

                            <Button class=" bg-green-900 text-xs" type="button" @click="openRegisterCall">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" class="feather feather-phone mr-2">
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z">
                                    </path>
                                </svg>

                                Register Call
                            </Button>
                            <Button class=" bg-green-500 text-xs" type="button" @click="openSchedule">

                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24"
                                    fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                    stroke-linejoin="round" class="feather feather-bell mr-2">
                                    <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                                    <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                                </svg>

                                Schedule Meeting
                            </Button>

                            <Button class="bg-blue-800 text-xs">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path
                                        d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z">
                                    </path>
                                    <path fill-rule="evenodd"
                                        d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
                                        clip-rule="evenodd"></path>
                                </svg>
                            </Button>
                            <Button class="bg-red-500">
                                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                        d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                                        clip-rule="evenodd"></path>
                                </svg>

                            </Button>
                        </div>
                    </TableCell>
                </TableRow>
            </TableBody>
        </Table>

        <SideDrawer v-if="showOverlay" @close-modal="closeModal" />
        <RegisterCall v-if="showRegisterCall" @close-modal="closeRegisterCall" />
        <ScheduleMeeting v-if="showScheduleMeeting" @close-modal="closeSchedule" />
    </div>
</template>

<script setup lang="ts">
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ref } from 'vue';
import AddProspectsModal from '~/components/dashboard/AddProspectsModal.vue';
import RegisterCall from '~/components/dashboard/prospects/RegisterCall.vue';
import ScheduleMeeting from '~/components/dashboard/prospects/ScheduleMeeting.vue';
import SideDrawer from '~/components/dashboard/prospects/SideDrawer.vue';

const showOverlay = ref<boolean>(false)
const showRegisterCall = ref<boolean>(false)
const showScheduleMeeting = ref<boolean>(false)

function openRegisterCall() {
    showRegisterCall.value = true
}

function closeRegisterCall() {
    showRegisterCall.value = false
}

function openSchedule() {
    showScheduleMeeting.value = true
}

function closeSchedule() {
    showScheduleMeeting.value = false
}

function onSendMessagePress() {
    console.log('Clicked')
    showOverlay.value = true
}

function closeModal() {
    showOverlay.value = false
}


definePageMeta({
    layout: 'dashboard'
})

</script>