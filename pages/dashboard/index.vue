<template>
    <div>

        <div class="flex flex-row gap-5 mb-5">
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Realtors</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">13</span>
                    <div>
                        <p>Registered: <b> 378</b></p>
                        <p>Activated: <b>378</b></p>
                        <p>Active: <b>378</b></p>
                    </div>
                    
                </CardContent>
            </Card>
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Houses</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">16</span>
                    <div class="mt-5">
                        <p>Total: <b> 378</b></p>
                        <p>Available: <b>78</b></p>
                    </div>
                </CardContent>
            </Card>
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Users</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">16</span>
                    <div class="mt-5">
                        <p>Registered: <b> 378</b></p>
                        <p>Activated: <b>78</b></p>
                    </div>
                </CardContent>
            </Card>
        </div>
        <div class="flex flex-row gap-5 mb-5">
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Support Tickets</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">1</span>
                </CardContent>
            </Card>
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Estates</CardTitle>
                </CardHeader>
                <CardContent class="flex">
                    <span class="text-4xl font-semibold">13</span>
                </CardContent>
                
            </Card>
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Complaints</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">13</span>
                </CardContent>
            </Card>
        </div>
        <div class="flex flex-row gap-5">
            <Card class="flex-1">
                <CardHeader>
                    <CardTitle>Prospects</CardTitle>
                </CardHeader>
                <CardContent>
                    <span class="text-4xl font-semibold">290</span>
                </CardContent>
            </Card>
            <div class="flex-1"></div>
            <div class="flex-1"></div>
        </div>
    </div>
</template>

<script setup>
definePageMeta({
    layout: 'dashboard'
})
</script>